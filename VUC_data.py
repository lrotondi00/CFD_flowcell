# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

#### import the simple module from the paraview
from paraview.simple import *
import sys
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Check if a folder path argument was provided
if len(sys.argv) < 2:
    print("Error: No folder path provided.")
    sys.exit(1)

# Get the folder path from the script arguments
folder_path = sys.argv[1]

# Verify that the provided folder path exists
if not os.path.isdir(folder_path):
    print(f"Error: The folder path '{folder_path}' does not exist.")
    sys.exit(1)

# Construct the file path for the OpenFOAM file
foam_file_path = os.path.join(folder_path, "pv.foam")

# Verify that the OpenFOAM file exists
if not os.path.isfile(foam_file_path):
    print(f"Error: The OpenFOAM file '{foam_file_path}' does not exist.")
    sys.exit(1)

# Load the OpenFOAM data
pvfoam = OpenFOAMReader(FileName=foam_file_path)
pvfoam.UpdatePipeline()

pvfoam.MeshRegions = ['internalMesh']
pvfoam.CellArrays = ['U', 'p']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
pvfoamDisplay = Show(pvfoam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
pvfoamDisplay.Representation = 'Surface'
pvfoamDisplay.ColorArrayName = ['POINTS', 'p']
pvfoamDisplay.LookupTable = pLUT
pvfoamDisplay.SelectTCoordArray = 'None'
pvfoamDisplay.SelectNormalArray = 'None'
pvfoamDisplay.SelectTangentArray = 'None'
pvfoamDisplay.OSPRayScaleArray = 'p'
pvfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pvfoamDisplay.SelectOrientationVectors = 'U'
pvfoamDisplay.ScaleFactor = 0.006228060461580753
pvfoamDisplay.SelectScaleArray = 'p'
pvfoamDisplay.GlyphType = 'Arrow'
pvfoamDisplay.GlyphTableIndexArray = 'p'
pvfoamDisplay.GaussianRadius = 0.0003114030230790377
pvfoamDisplay.SetScaleArray = ['POINTS', 'p']
pvfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pvfoamDisplay.OpacityArray = ['POINTS', 'p']
pvfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pvfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
pvfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
pvfoamDisplay.ScalarOpacityFunction = pPWF
pvfoamDisplay.ScalarOpacityUnitDistance = 0.0021027127428564257
pvfoamDisplay.OpacityArrayName = ['POINTS', 'p']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pvfoamDisplay.OSPRayScaleFunction.Points = [-2.4350283638341352e-06, 0.0, 0.5, 0.0, 9.474614489590749e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pvfoamDisplay.ScaleTransferFunction.Points = [100.03143310546875, 0.0, 0.5, 0.0, 100.64828491210938, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pvfoamDisplay.OpacityTransferFunction.Points = [100.03143310546875, 0.0, 0.5, 0.0, 100.64828491210938, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
pvfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=pvfoam)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.018232605420053005, 0.015181808732450008, -0.021243970841169357]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.018232605420053005, 0.015181808732450008, -0.021243970841169357]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.01823260262608528, 0.01526332926005125, -0.00771923203450823] #Serie 5.0
#slice1.SliceType.Origin = [0.01823260262608528, 0.01526332926005125, -0.0015188344353642] #Serie 5.1
#slice1.SliceType.Origin = [0.01823260262608528, 0.01526332926005125, -0.0099910384863094] #Serie 5.2
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.005277685448527337
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.GaussianRadius = 0.0002638842724263668
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [-2.4350283638341352e-06, 0.0, 0.5, 0.0, 9.474614489590749e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [100.19768524169922, 0.0, 0.5, 0.0, 100.64542388916016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [100.19768524169922, 0.0, 0.5, 0.0, 100.64542388916016, 1.0, 0.5, 0.0]

# hide data in view
Hide(pvfoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=slice1)
clip1.ClipType = 'Box'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 100.42155456542969

# init the 'Box' selected for 'ClipType'
clip1.ClipType.Position = [-0.008154943585395813, -0.003224465064704418, -0.007719232235103846]
clip1.ClipType.Length = [0.05277685448527336, 0.04637922998517752, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.018233483657240868, 0.01996514992788434, -0.007719232235103846]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1
clip1.ClipType = 'Cylinder'

# Properties modified on clip1.ClipType
clip1.ClipType.Center = [0.0182327264919877, 0.01304, -0.00741216680034995] #serie 5.0
#clip1.ClipType.Center = [0.0192942216910554, -0.029252274771619, 0.01] #serie 5.1
#clip1.ClipType.Center = [0.0213007245827791, 0.0147318755348064, -0.00784273538738489] #serie 5.2
clip1.ClipType.Axis = [0.0, 0.0, 1.0]
clip1.ClipType.Radius = 0.008

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 0.0016998572275042534
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.GaussianRadius = 8.499286137521267e-05
clip1Display.SetScaleArray = ['POINTS', 'p']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'p']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 0.0018740500903269704
clip1Display.OpacityArrayName = ['POINTS', 'p']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [-2.4350283638341352e-06, 0.0, 0.5, 0.0, 9.474614489590749e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [100.49536895751953, 0.0, 0.5, 0.0, 100.64542388916016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [100.49536895751953, 0.0, 0.5, 0.0, 100.64542388916016, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=clip1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = ['POINTS', 'p']
extractSurface1Display.LookupTable = pLUT
extractSurface1Display.SelectTCoordArray = 'None'
extractSurface1Display.SelectNormalArray = 'None'
extractSurface1Display.SelectTangentArray = 'None'
extractSurface1Display.OSPRayScaleArray = 'p'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'U'
extractSurface1Display.ScaleFactor = 0.0016998572275042534
extractSurface1Display.SelectScaleArray = 'p'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'p'
extractSurface1Display.GaussianRadius = 8.499286137521267e-05
extractSurface1Display.SetScaleArray = ['POINTS', 'p']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'p']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface1Display.OSPRayScaleFunction.Points = [-2.4350283638341352e-06, 0.0, 0.5, 0.0, 9.474614489590749e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [100.49536895751953, 0.0, 0.5, 0.0, 100.64542388916016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [100.49536895751953, 0.0, 0.5, 0.0, 100.64542388916016, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
extractSurface1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# create a new 'Mesh Quality'
meshQuality1 = MeshQuality(registrationName='MeshQuality1', Input=extractSurface1)

# Properties modified on meshQuality1
meshQuality1.TriangleQualityMeasure = 'Area'
meshQuality1.QuadQualityMeasure = 'Area'

# show data in view
meshQuality1Display = Show(meshQuality1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
meshQuality1Display.Representation = 'Surface'
meshQuality1Display.ColorArrayName = ['POINTS', 'p']
meshQuality1Display.LookupTable = pLUT
meshQuality1Display.SelectTCoordArray = 'None'
meshQuality1Display.SelectNormalArray = 'None'
meshQuality1Display.SelectTangentArray = 'None'
meshQuality1Display.OSPRayScaleArray = 'p'
meshQuality1Display.OSPRayScaleFunction = 'PiecewiseFunction'
meshQuality1Display.SelectOrientationVectors = 'U'
meshQuality1Display.ScaleFactor = 0.0016998572275042534
meshQuality1Display.SelectScaleArray = 'p'
meshQuality1Display.GlyphType = 'Arrow'
meshQuality1Display.GlyphTableIndexArray = 'p'
meshQuality1Display.GaussianRadius = 8.499286137521267e-05
meshQuality1Display.SetScaleArray = ['POINTS', 'p']
meshQuality1Display.ScaleTransferFunction = 'PiecewiseFunction'
meshQuality1Display.OpacityArray = ['POINTS', 'p']
meshQuality1Display.OpacityTransferFunction = 'PiecewiseFunction'
meshQuality1Display.DataAxesGrid = 'GridAxesRepresentation'
meshQuality1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
meshQuality1Display.OSPRayScaleFunction.Points = [-2.4350283638341352e-06, 0.0, 0.5, 0.0, 9.474614489590749e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
meshQuality1Display.ScaleTransferFunction.Points = [100.4747543334961, 0.0, 0.5, 0.0, 100.64684295654297, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
meshQuality1Display.OpacityTransferFunction.Points = [100.4747543334961, 0.0, 0.5, 0.0, 100.64684295654297, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
meshQuality1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create new layout object 'Layout #2'
layout2 = CreateLayout(name='Layout #2')

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
meshQuality1Display_1 = Show(meshQuality1, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout2, hint=0)

# Properties modified on spreadSheetView1
spreadSheetView1.FieldAssociation = 'Cell Data'

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Block Name']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Block Name', 'Cell ID']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Block Name', 'Cell ID', 'Cell Type']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Block Name', 'Cell ID', 'Cell Type', 'p']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Block Name', 'Cell ID', 'Cell Type', 'p', 'U_Magnitude']

# Define output file path for the export
output_file_path = os.path.join(folder_path, "VUC_data_foam.csv")

# export view
ExportView(output_file_path, view=spreadSheetView1, RealNumberNotation='Mixed',
    RealNumberPrecision=12)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayoutByName("Layout #1")

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1359, 733)

# layout/tab size in pixels
layout2.SetSize(400, 400)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.03056383221291335, 0.013106056425358163, 0.04762680389421476]
renderView1.CameraFocalPoint = [0.024228155491057005, 0.014172559847385559, 0.0122416008128941]
renderView1.CameraViewUp = [-0.9269128416160832, 0.33147111552607517, 0.1759530722070441]
renderView1.CameraParallelScale = 0.05175227567381273

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).