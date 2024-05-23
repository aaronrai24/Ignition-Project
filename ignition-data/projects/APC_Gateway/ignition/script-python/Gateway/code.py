# save loadout log -- returns number of records affected
def insertLoadout(LocCode, SiloNumber, LoadoutDate, LoadoutWeight, LoadoutTemperature):
	call = system.db.createSProcCall("InsertLoadoutLog")
	call.registerReturnParam(system.db.INTEGER)
	call.registerInParam('LocationCode',system.db.NVARCHAR,LocCode)
	call.registerInParam('SiloNumber',system.db.INTEGER,SiloNumber)
	call.registerInParam('LoadoutDate',system.db.VARCHAR ,LoadoutDate)
	call.registerInParam('Weight',system.db.FLOAT,LoadoutWeight)
	call.registerInParam('Temperature',system.db.FLOAT,LoadoutTemperature)
	system.db.execSProcCall(call)
	return call.getReturnValue()
