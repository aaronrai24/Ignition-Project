logger = system.util.getLogger("MyEventLogger")
def logme(event):
	logger.debugf("Debug %s", event)