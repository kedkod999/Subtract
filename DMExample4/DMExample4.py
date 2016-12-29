
import units

def createMyFeature(ag):
	ExtAPI.CreateFeature("Subtract")

def generateSubtract(feature,fct):

	Instrument = feature.Properties["Instrument"].Value.Entities
	Target = feature.Properties["Target"].Value.Entities
	Delete = feature.Properties["DeleteInstrument"].Value
	Change = feature.Properties["Change"].Value
	
	for body in ExtAPI.DataModel.GeoData.Parts: 
		ExtAPI.Log.WriteMessage(body.Name)
	
	if Change == "Yes":
		sw = Target
		Target = Instrument
		Instrument = sw

	bodies = []
	
	builder = ExtAPI.DataModel.GeometryBuilder
	
	extrudeOperation = builder.Operations.CreateSubtractOperation(Instrument)
	bodies = extrudeOperation.ApplyTo(Target)
	feature.Bodies = bodies
	feature.MaterialType = MaterialTypeEnum.Freeze

	if Delete == "Yes":
		for Entitie in Instrument:
			builder.Operations.Tools.DeleteBody(Entitie)
	for Entitie2 in Target:
		builder.Operations.Tools.DeleteBody(Entitie2)	
	
	return True
