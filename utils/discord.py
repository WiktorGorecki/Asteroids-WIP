import discordsdk as dsdk
from utils.settings import readSettings

settings = readSettings()
if settings["discord"]:
    app = dsdk.Discord(1110253474244989028, dsdk.CreateFlags.default)
    activity_manager = app.get_activity_manager()

def getApp():
    return app

def setActivity():
    print("Debug: Trying to set Discord activity")
    if settings["discord"]:
        try:
            activity = dsdk.Activity()
            activity.state = "Playing WIP-Asteroids"
            activity_manager.update_activity(activity, callback)
        except:
            print("     Discord exception")

def callback(result):
    if result == dsdk.Result.ok:
        print("Successfully set the activity!")
    else:
        raise Exception(result)