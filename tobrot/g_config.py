from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1436730490:AAFpVNY8ki0nzaLW8jotAQdca7bd3qAf2Zs"
    APP_ID = 1383845
    API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
    OWNER_ID = 1131653685
    AUTH_CHANNEL = [-1001266398622]
    DESTINATION_FOLDER = "DOWNLOAD" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
