"""
Elasticsearch's More Like This (MLT) query is a powerful feature that helps you find documents that are similar to a
given set of documents. It's often used to implement features like "customers who bought this also bought these" in
e-commerce applications, or "related articles" in content-driven websites.

Here's an in-depth explanation of how MLT works:

Document Selection: The MLT query begins by selecting one or more documents to act as the basis for finding similar
documents. This can be done by providing the text directly, or by specifying the index and document ID of the documents
you want to match.

Term Selection: Next, Elasticsearch breaks the text of these documents down into individual terms
(words, in most cases). This is done using the same analyzer that was used when indexing the document. From these terms,
a subset is selected to be used in the actual query. This selection is done based on term frequency (how often the term
appears in the selected document) and document frequency (how often the term appears in all documents in the index).

By default, Elasticsearch chooses terms that have a term frequency of at least 2, and a document frequency of no more
than 5% of the total number of documents in the index. However, these settings can be customized with the min_term_freq,
max_query_terms, and min_doc_freq parameters.

Query Construction: The selected terms are then used to construct a bool query, with each term wrapped in a term query
and added to the should clause of the bool query. This means that documents will be considered a match if they contain
any of the selected terms.

Scoring: As with any Elasticsearch query, the results are then scored based on how well they match the query.
In the case of MLT, this score will be higher for documents that contain more of the selected terms, and/or for terms
that were more frequent in the original document(s). The score will also be influenced by the document frequency of the
terms; rarer terms will contribute more to the score than common ones.

The exact scoring algorithm used is the TF-IDF (Term Frequency-Inverse Document Frequency), which balances the
term frequency (the number of times a term appears in a document) against the inverse document frequency (a measure of
how common or rare the term is across the entire document set).

Result Ranking: The matching documents are then sorted by score, and the top N are returned, where N is specified by
the size parameter.

By adjusting the parameters of the MLT query, you can tune the balance between recall (returning as many relevant
documents as possible) and precision (only returning very similar documents), as well as control the computational
load of the query. For example, increasing max_query_terms will potentially return more results, but the query will
take longer to execute.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, CustomPermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MoreLikeThis
from elasticsearch_dsl.connections import connections
import os
os.environ["ELASTIC_CLIENT_IGNORE_VERSION_CHECK"] = "true"
os.environ['ELASTIC_CLIENT_DISABLE_PRODUCT_CHECK'] = 'true'


class MoreLikeThisView(CustomPermissionRequiredMixin, UserPassesTestMixin, TemplateView, LoginRequiredMixin,
                       AdminMenuMixin):
    template_name = "backend/autocomplete/morelikethis.html"
    permission_menu = 'morelikethis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search_value', '')
        print(search_value)
        es_client = connections.get_connection()

        if es_client.ping() and search_value:
            print("Using ES")

            s = Search(using=es_client, index="es_test_index")
            s = s.query(MoreLikeThis(like=search_value, fields=['title', 'content', 'author'], min_term_freq=1))
            s = s.source(exclude=["content"])
            s = s.extra(explain=True)
            print(s.to_dict())
            response = s.execute()
            print(response)

            # Extract the title, content and author values from the hits
            suggestions = [{'title': hit.title, 'author': hit.author} for hit in response]
            print(suggestions)
            return JsonResponse(suggestions, safe=False)

        return super().get(request, *args, **kwargs)
