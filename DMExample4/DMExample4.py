
import units

def createMyFeature(ag):
	ExtAPI.CreateFeature("BoxFeature")

def generateBoxGeometry(feature,fct):
	ExtAPI.Log.WriteMessage("Generating MyFeature...")
    
    # Collect all property values in meter unit
	fromUnit, toUnit = ExtAPI.DataModel.CurrentUnitFromQuantityName("Length"), "m"
    
    #Get Length width and Thickness of the Box
	Center= units.ConvertUnit(feature.Properties["Center"].Value, fromUnit, toUnit)
	Thickness = units.ConvertUnit(feature.Properties["Thickness"].Value, fromUnit, toUnit)
	Width = units.ConvertUnit(feature.Properties["Width"].Value, fromUnit, toUnit)
	ExtAPI.Log.WriteMessage(Center.ToString())
	ExtAPI.Log.WriteMessage(Thickness.ToString())
	ExtAPI.Log.WriteMessage(Width.ToString())
	
	bodies = []
	bodies1 = []
	bodies2 = []
	#builder1 = ExtAPI.DataModel.GeometryBuilder
	#squarePri1 = builder1.Primitives.Sheet.CreatePolygon([0.,0.,0.,1.,0.,0.,1.,1.,0.,0.,1.,0.])
	#squareBody1 = squarePri1.Generate()
	#extrudeOperation1 = builder1.Operations.CreateExtrudeOperation([0.,0.,-1.],10.)
	#bodies = extrudeOperation1.ApplyTo(squareBody1)
	#feature.Bodies = bodies
	#feature.MaterialType = MaterialTypeEnum.Freeze
	
	#builder = ExtAPI.DataModel.GeometryBuilder
	#squarePri = builder.Primitives.Sheet.CreatePolygon([0.,0.,0.,3.,0.,0.,3.,3.,0.,0.,3.,0.])
	#squareBody = squarePri.Generate()
	#extrudeOperation = builder.Operations.CreateExtrudeOperation([0.,0.,1.],3.)
	#bodies2 = extrudeOperation.ApplyTo(squareBody)
	#bodies.Add(bodies2)
	#feature.Bodies = bodies2
	#feature.MaterialType = MaterialTypeEnum.Freeze

	builder = ExtAPI.DataModel.GeometryBuilder
	point1 = [0.,0.,0.]
	point2 = [1.,2.,2.]
	
	primitive = ExtAPI.DataModel.GeometryBuilder.Primitives
	box1 = primitive.Solid.CreateBox(point1, point2)
	box1_generated = box1.Generate()
	bodies.Add(box1_generated)
	feature.Bodies = bodies
	feature.MaterialType = MaterialTypeEnum.Freeze
	
	point3 = [-0.5,-1.,-1.]
	point4 = [0.5,1.,1.]
	box2 = primitive.Solid.CreateBox(point3, point4)
	box2_generated = box2.Generate()
	bodies1.Add(box2_generated)
	feature.Bodies = bodies1
	feature.MaterialType = MaterialTypeEnum.Freeze
	
	#squarePri = builder.Primitives.Sheet.CreatePolygon([0.,0.,0.,0.5,0.,0.,0.5,0.5,0.,0.,0.5,0.])
	#squareBody = squarePri.Generate()
	extrudeOperation = builder.Operations.CreateSubtractOperation(bodies1)
	bodies2 = extrudeOperation.ApplyTo(bodies)
	feature.Bodies = bodies2
	feature.MaterialType = MaterialTypeEnum.Freeze

	#builder = ExtAPI.DataModel.GeometryBuilder
	#width = 1.0
	#height = 2.0
	#primitive = ExtAPI.DataModel.GeometryBuilder.Primitives
	#cylinder = primitive.Solid.CreateSphere([0.,0.,0.],width)
	#cylinder_generated = cylinder.Generate()
	#bodies.Add(cylinder_generated)
	#feature.Bodies = bodies
	#feature.MaterialType = MaterialTypeEnum.Freeze
	
	return True
