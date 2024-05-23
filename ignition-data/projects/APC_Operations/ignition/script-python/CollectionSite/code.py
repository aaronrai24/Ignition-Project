# Collection Site Routines 
def GetStatusTabs(Username):
	cc=system.db.createSProcCall('GetStatusTabs')
	cc.registerInParam('UserName', system.db.NVARCHAR, Username)
	cc.registerReturnParam(system.db.NVARCHAR)
	system.db.execSProcCall(cc)
	s = cc.getResultSet()
	cols=["NAME","SELECTED_IMAGE_VERTICAL_ALIGNMENT","DISPLAY_NAME","ENABLED","HIDDEN","HOVER_COLOR","SELECTED_IMAGE_PATH","SELECTED_IMAGE_HORIZONTAL_ALIGNMENT","SELECTED_FORGROUND_COLOR"]
	data=[]	
	if s.getRowCount() > 0:
		for i, tn in enumerate(s.getValueAt(0,0).split(';')):
			data.append(["Tab " + str(i),"0",tn,"true","false","color(204,255,255,255)","","-1","color(0,0,0,255)"])
	return system.dataset.toDataSet(cols, data)
	
def SaveStatusTabs(Username, TabNames):
	cc=system.db.createSProcCall('SaveStatusTabs')
	cc.registerInParam('UserName', system.db.NVARCHAR, Username)
	cc.registerInParam('Tabs', system.db.NVARCHAR, TabNames)
	cc.registerReturnParam(system.db.INTEGER)
	system.db.execSProcCall(cc)
	return

def GetStatusTabDataset(Username, Tab):
	cc=system.db.createSProcCall('GetStatusTabPaths')
	cc.registerInParam('UserName', system.db.NVARCHAR, Username)
	cc.registerInParam('Tab', system.db.NVARCHAR, Tab)
	cc.registerReturnParam(system.db.INTEGER)
	system.db.execSProcCall(cc)
	s = cc.getResultSet()
	cols=["CollectionLocationPath"]
	data=[]
	for i,p in enumerate(s.getValueAt(0,0).split(';')):
		data.append([p.strip()])
	return system.dataset.toDataSet(cols, data)

def SaveStatusTabDataset(Username, Tab, Data):
	cc=system.db.createSProcCall('SaveStatusTabPaths')
	cc.registerInParam('UserName', system.db.NVARCHAR, Username)
	cc.registerInParam('Tab', system.db.NVARCHAR, Tab)
	dv=nv=''
	cc.registerInParam('Paths', system.db.NVARCHAR, Data)
	cc.registerReturnParam(system.db.INTEGER)
	system.db.execSProcCall(cc)
	return

def DeleteStatusTab(Username, Tab):
	cc=system.db.createSProcCall('DeleteStatusTab')
	cc.registerInParam('UserName', system.db.NVARCHAR, Username)
	if Tab<>None:
		cc.registerInParam('Tab', system.db.NVARCHAR, Tab)
	cc.registerReturnParam(system.db.INTEGER)
	system.db.execSProcCall(cc)
	return