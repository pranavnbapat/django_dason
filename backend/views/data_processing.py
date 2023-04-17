import pandas as pd
import os
import random
import string
from django.conf import settings
import datetime


def generate_random_filename(length: int):
    """Generate a random alphanumeric filename with the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def process_dashboard_data():
    df_users_devices = pd.read_csv("data/analytics/device_specific_visitors.csv")

    df_users_over_period = pd.read_csv("data/analytics/users_visiting_over_year.csv")
    df_users_over_period['Date'] = pd.to_datetime(df_users_over_period['Date'], format='%b %d, %Y')
    df_users_over_period = df_users_over_period.groupby(pd.Grouper(key='Date', freq='M')).sum()
    df_users_over_period = df_users_over_period.reset_index()
    df_users_over_period['Date'] = df_users_over_period['Date'].dt.strftime('%b %Y')

    df_new_ret_vis = pd.read_csv("data/analytics/new_ret_users.csv")

    df_lang_spec_new_ret_vis = pd.read_csv("data/analytics/lang_specific_new_ret_users.csv")
    df_lang_spec_new_ret_vis = df_lang_spec_new_ret_vis.head(20)

    df_top_acq_channels = pd.read_csv("data/analytics/top_acq_channels.csv")

    df_new_ret_users_timeseries = pd.read_csv("data/analytics/new_ret_users_timeseries.csv")
    df_new_ret_users_timeseries['Date'] = pd.to_datetime(df_new_ret_users_timeseries['Date'], format='%b %d, %Y')
    df_new_ret_users_timeseries = df_new_ret_users_timeseries.groupby(pd.Grouper(key='Date', freq='M')).sum()
    df_new_ret_users_timeseries = df_new_ret_users_timeseries.reset_index()
    df_new_ret_users_timeseries['Date'] = df_new_ret_users_timeseries['Date'].dt.strftime('%b %Y')

    df_page_popularity = pd.read_csv("data/analytics/page_popularity.csv")
    df_page_popularity = df_page_popularity.head(10)

    data = {'devices': list(df_users_devices['Device']), 'users': list(df_users_devices['Users'])}
    data_users_over_period = {'date': list(df_users_over_period['Date']),
                              'users': list(df_users_over_period['Users'])}
    data_new_ret_vis = {'user_type': list(df_new_ret_vis['User Type']),
                        'sessions': list(df_new_ret_vis['Sessions'])}
    data_lang_spec_new_ret_vis = {'lang': list(df_lang_spec_new_ret_vis['Language']),
                                  'users': list(df_lang_spec_new_ret_vis['Users']),
                                  'new_users': list(df_lang_spec_new_ret_vis['New Users'])}
    data_top_acq_channels = {'channel': list(df_top_acq_channels['Default Channel Grouping']),
                             'users': list(df_top_acq_channels['Users'])}
    data_new_ret_users_timeseries = {'date': list(df_new_ret_users_timeseries['Date']),
                                     'users': list(df_new_ret_users_timeseries['Users']),
                                     'new_users': list(df_new_ret_users_timeseries['New Users'])}
    data_page_popularity = {'page': list(df_page_popularity['Page']),
                            'pageviews': list(df_page_popularity['Pageviews'])}

    return {
        'data_json': data,
        'data_users_over_period': data_users_over_period,
        'data_new_ret_vis': data_new_ret_vis,
        'data_lang_spec_new_ret_vis': data_lang_spec_new_ret_vis,
        'data_top_acq_channels': data_top_acq_channels,
        'data_new_ret_users_timeseries': data_new_ret_users_timeseries,
        'data_page_popularity': data_page_popularity,
    }


def manage_avatar_upload(file, length=20):
    os.makedirs(settings.AVATAR_PATH, exist_ok=True)
    random_filename = generate_random_filename(length)
    _, file_ext = os.path.splitext(file.name)
    avatar = random_filename + file_ext

    with open(os.path.join(settings.AVATAR_PATH, avatar), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return avatar


def nested_list_to_csv(nested_list):
    def flatten_list(nested_list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

    flat_list = flatten_list(nested_list)
    return ', '.join(str(item) for item in flat_list)


def file_async_upload(request, dest, file_type):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')

        if uploaded_file:
            # Check if the file type matches the expected file_type
            if uploaded_file.content_type != file_type:
                return {"status": "error", "message": "Invalid file type"}

            # Check if the filename is longer than 200 characters
            if len(uploaded_file.name) > 200:
                return {"status": "error", "message": "Filename too long (more than 200 characters)"}

            # Append a timestamp to the filename
            filename, ext = os.path.splitext(uploaded_file.name)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            new_filename = f"{timestamp}{ext}"

            # Save the file to the specified folder
            save_path = os.path.join(settings.BASE_DIR, dest, new_filename)
            with open(save_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # return JsonResponse({"status": "success", "message": "File uploaded successfully"})
            return {"status": "success", "old_filename": uploaded_file.name, "new_filename": new_filename}

    return {"status": "error", "message": "Invalid file type"}
    # return JsonResponse({"status": "error", "message": "Invalid request method"})


# def rotation_angle(image):
#     """
#         Determine the rotation angle of the text in an image using the Radon Transform.
#
#         :param image: The image to analyze.
#         :type image: Image.Image
#         :returns: The rotation angle.
#         :rtype: float
#         """
#     # Convert the image to grayscale
#     gray = image.convert('L')
#
#     # Convert the grayscale image to a numpy array
#     img_np = np.array(gray)
#
#     # Compute the Radon transform
#     rt = radon(img_np)
#
#     # Determine the rotation angle
#     angle = np.argmax(np.sum(rt, axis=0))
#     return angle
#
