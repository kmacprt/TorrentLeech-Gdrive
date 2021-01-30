from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1436730490:AAFpVNY8ki0nzaLW8jotAQdca7bd3qAf2Zs"
    APP_ID = 1383845
    API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
    OWNER_ID = 1156597097
    AUTH_CHANNEL = [-1001266398622]
    DESTINATION_FOLDER = "DOWNLOAD" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[Kavindu aj]
type = drive
client_id = 689266221247-cks6608mg9oc4b6sdju953oah1o6cmve.apps.googleusercontent.com
client_secret = lG1zuSUQs4KuEm6p0JnIJo5n
scope = drive
root_folder_id =
token = {"access_token":"ya29.a0AfH6SMDN-6z_n-j3W7Ftkj_Xnp2BXZczmHyXQcfS7F8I3c7XxAUJwBjxv40mbfqKgpjLu-zTk0e0pzj60p-e8fbRGCmOUMniYPW1XqlXPZwabJBC3WyQic5r736lUtzkexVIbFYngHEgcFnsMNBUmtwz9A5ft_4mIkjJm0QfUwA","token_type":"Bearer","refresh_token":"1//0g695p0pmqnIOCgYIARAAGBASNwF-L9IrHu6FcCtrry52Dbl_aMFjZnWsKObLgKreDOCXjtt0LaKSjWqQP9DjDoB9nglmz3HseYI","expiry":"2021-01-29T05:56:56.0250148-08:00"}
team_drive = 0AEnYW_mILPIFUk9PVA
"""
