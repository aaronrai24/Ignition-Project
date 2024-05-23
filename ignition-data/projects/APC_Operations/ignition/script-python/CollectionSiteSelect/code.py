#Routines to simplify the CollectionSiteSelect window 
def Initialize(event):
	#get username and roles
	myname=system.security.getUsername()
	myroles=system.security.getRoles()
	#with logistics role we have tabs
	#with fieldtechmanager role we have field techs
	#so get the tabs or user and save the dataset
	tabs=[]
	if 'logistics' in (r.lower() for r in myroles):
		tabDS = CollectionSite.GetStatusTabs(myname)
		for rowIndex in range(tabDS.getRowCount()):
			tabs.append([tabDS.getValueAt(rowIndex,"DISPLAY_NAME")])
		system.gui.getParentWindow(event).getComponentForPath('Root Container').ShowTabs=True
		system.gui.getParentWindow(event).getComponentForPath('Root Container').TabList = system.dataset.toDataSet(['Path'], tabs)
	elif 'fieldtechmanager' in (r.lower() for r in myroles):
		system.gui.getParentWindow(event).getComponentForPath('Root Container').ShowTabs=False
		fldtechs=ScanForFieldTechs()
		system.gui.getParentWindow(event).getComponentForPath('Root Container').UserList = system.dataset.toDataSet(['username','Name'],fldtechs)
	#
	#update the all locations dataset
	locations = system.tag.browseTags(parentPath = '', tagPath = '*',tagType = 'Folder',recursive=False)
	tagDS = []
	for loc in locations:
		show = system.tag.read(loc.fullPath + '/ShowLocation')
		if show.value:
			company = system.tag.read(loc.fullPath + '/Location Information/Company')
			city = system.tag.read(loc.fullPath + '/Location Information/City')
			tagDS.append([0, company.value + "  " + city.value, loc.fullPath])
	system.gui.getParentWindow(event).getComponentForPath('Root Container').CollectionSiteDS = system.dataset.toDataSet(["Select","Location","Path"],tagDS)
	# mark the change field as done
	system.gui.getParentWindow(event).getComponentForPath('Root Container').Change=False

def ScanForFieldTechs():
	fldtechs=[]
	users=system.user.getUsers('default')
	for user in users:
		uroles=user.getRoles()
		if 'fieldtech' in (r.lower() for r in uroles):
			fldtechs.append([user.get('username'),user.get('firstname') + ' ' +user.get('lastname')])
	return fldtechs

def DeleteOldFldTechs():
	return