#!/usr/bin/env python
# coding: utf-8

from paraview.simple import *
import os

sizes = [30] # diameter in nm

elongations = [0] # elongations in %

#material = "taenite_highT"

#geometry = "triaxial_ellipsoid"

home = 'C:\\Users\\josea\\Desktop\\Documents\\PhD\\swiss_cheese\\cubic\\0_holes_R1\\T20\\'

##C:\Users\josea\Desktop\Documents\PhD\Taenite_HighT\python_scripts\taenite_highT

for elongation in elongations:
    if elongation < 10:
        elongation = '0{}'.format(elongation)
    for size in sizes:            
        groundstates_path = os.path.join(home,
                                        'groundstates',
                                        str(size))
            #PATH = 'D:/Taenite/jupyter/data_{}/E{}/groundstates/{}'.format(geometry, elongation, size)
        if len(os.listdir(groundstates_path)) == 0:
            pass
        else:
            i = 1
            for FILE in os.listdir(groundstates_path):
                groundstate_plots_dir = os.path.join(home,
                                                    'plots',
                                                    str(size))
                    #new_dir = 'D:/Taenite/jupyter/data_{}/E{}/plots/{}'.format(geometry, elongation, size)
                #groundstate_plot = os.path.join(groundstate_plots_dir,
                                                #'{}.png'.format(i))
                    #groundstate_plots_dir + '/{}.png'.format(i)
                    # if os.path.exists(finalpath):
                    # pass
                    # else:
                if os.path.splitext(FILE)[1] == '.tec':
                    filepath = os.path.join(groundstates_path, FILE)
                        # paraview.simple._DisableFirstRenderCameraReset()8:46 PM 4/15/2021

                        # create a new 'Tecplot Reader'
                    file = TecplotReader(FileNames=[filepath])
                    file.DataArrayStatus = ['Mx', 'My', 'Mz', 'SD']

                        # get active view
                    renderView1 = GetActiveViewOrCreate('RenderView')
                        # uncomment following to set a specific view size
                        # renderView1.ViewSize = [989, 541]

                        # show data in view
                    fileDisplay = Show(file, renderView1)
                        # trace defaults for the display properties.
                    fileDisplay.ColorArrayName = [None, '']
                    fileDisplay.OSPRayScaleArray = 'Mx'
                    fileDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
                    fileDisplay.GlyphType = 'Arrow'
                    fileDisplay.ScalarOpacityUnitDistance = 0.003356151409034327
                    fileDisplay.SetScaleArray = ['POINTS', 'Mx']
                    fileDisplay.ScaleTransferFunction = 'PiecewiseFunction'
                    fileDisplay.OpacityArray = ['POINTS', 'Mx']
                    fileDisplay.OpacityTransferFunction = 'PiecewiseFunction'

                        # reset view to fit data
                    renderView1.ResetCamera()

                        # create a new 'Calculator'
                    calculator1 = Calculator(Input=file)
                    calculator1.Function = ''

                        # Properties modified on calculator1
                    calculator1.ResultArrayName = 'M'
                    calculator1.Function = 'Mx*iHat+My*jHat+Mz*kHat'

                        # show data in view
                    calculator1Display = Show(calculator1, renderView1)
                        # trace defaults for the display properties.
                    calculator1Display.ColorArrayName = [None, '']
                    calculator1Display.OSPRayScaleArray = 'M'
                    calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
                    calculator1Display.GlyphType = 'Arrow'
                    calculator1Display.ScalarOpacityUnitDistance = 0.003356151409034327
                    calculator1Display.SetScaleArray = ['POINTS', 'Mx']
                    calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
                    calculator1Display.OpacityArray = ['POINTS', 'Mx']
                    calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'

                        # hide data in view
                    Hide(file, renderView1)

                        # create a new 'Glyph'
                    glyph1 = Glyph(Input=calculator1,
                                    GlyphType='Arrow')
                    glyph1.Scalars = ['POINTS', 'Mx']
                    glyph1.Vectors = ['POINTS', 'M']
                    glyph1.ScaleFactor = 0.008999373018741609
                    glyph1.GlyphTransform = 'Transform2'

                        # Properties modified on glyph1
                    glyph1.ScaleFactor = 0.006389554843306542

                        # get color transfer function/color map for 'Mx'
                    mxLUT = GetColorTransferFunction('Mx')
                    mxLUT.RGBPoints = [-0.999984622001648, 0.231373, 0.298039, 0.752941, -0.1503884196281433, 0.865003,
                                        0.865003, 0.865003, 0.6992077827453613, 0.705882, 0.0156863, 0.14902]
                    mxLUT.ScalarRangeInitialized = 1.0

                        # show data in view
                    glyph1Display = Show(glyph1, renderView1)
                        # trace defaults for the display properties.
                    glyph1Display.ColorArrayName = ['POINTS', 'Mx']
                    glyph1Display.LookupTable = mxLUT
                    glyph1Display.OSPRayScaleArray = 'Mx'
                    glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
                    glyph1Display.GlyphType = 'Arrow'
                    glyph1Display.SetScaleArray = ['POINTS', 'Mx']
                    glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
                    glyph1Display.OpacityArray = ['POINTS', 'Mx']
                    glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'

                        # show color bar/color legend
                    glyph1Display.SetScalarBarVisibility(renderView1, True)

                        # get opacity transfer function/opacity map for 'Mx'
                    mxPWF = GetOpacityTransferFunction('Mx')
                    mxPWF.Points = [-0.999984622001648, 0.0, 0.5, 0.0, 0.6992077827453613, 1.0, 0.5, 0.0]
                    mxPWF.ScalarRangeInitialized = 1

                        # Properties modified on glyph1
                    glyph1.ScaleFactor = 0.006119573652744294

                        # Properties modified on glyph1
                    glyph1.ScaleFactor = 0.004499686509370804

                        # Rescale transfer function
                    mxLUT.RescaleTransferFunction(-1.0, 1.0)

                        # Rescale transfer function
                    mxPWF.RescaleTransferFunction(-1.0, 1.0)

                        # hide data in view
                    Hide(calculator1, renderView1)

                        # set active source
                    SetActiveSource(calculator1)

                        # create a new 'Gradient Of Unstructured DataSet'
                    gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=calculator1)
                    gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'M']

                        # Properties modified on gradientOfUnstructuredDataSet1
                    gradientOfUnstructuredDataSet1.ComputeVorticity = 1
                    gradientOfUnstructuredDataSet1.VorticityArrayName = 'V'

                        # show data in view
                    gradientOfUnstructuredDataSet1Display = Show(gradientOfUnstructuredDataSet1, renderView1)
                        # trace defaults for the display properties.
                    gradientOfUnstructuredDataSet1Display.ColorArrayName = [None, '']
                    gradientOfUnstructuredDataSet1Display.OSPRayScaleArray = 'Gradients'
                    gradientOfUnstructuredDataSet1Display.OSPRayScaleFunction = 'PiecewiseFunction'
                    gradientOfUnstructuredDataSet1Display.GlyphType = 'Arrow'
                    gradientOfUnstructuredDataSet1Display.ScalarOpacityUnitDistance = 0.003356151409034327
                    gradientOfUnstructuredDataSet1Display.SetScaleArray = ['POINTS', 'Mx']
                    gradientOfUnstructuredDataSet1Display.ScaleTransferFunction = 'PiecewiseFunction'
                    gradientOfUnstructuredDataSet1Display.OpacityArray = ['POINTS', 'Mx']
                    gradientOfUnstructuredDataSet1Display.OpacityTransferFunction = 'PiecewiseFunction'

                        # hide data in view
                    Hide(calculator1, renderView1)

                        # hide data in view
                    Hide(gradientOfUnstructuredDataSet1, renderView1)

                        # set active source
                    SetActiveSource(glyph1)

                        # set active source
                    SetActiveSource(calculator1)

                        # set active source
                    SetActiveSource(gradientOfUnstructuredDataSet1)

                        # create a new 'Calculator'
                    calculator2 = Calculator(Input=gradientOfUnstructuredDataSet1)
                    calculator2.Function = ''

                        # Properties modified on calculator2
                    calculator2.ResultArrayName = 'H'
                    calculator2.Function = 'M.V'

                        # get color transfer function/color map for 'H'
                    hLUT = GetColorTransferFunction('H')
                    hLUT.RGBPoints = [-8.908677584627712, 0.231373, 0.298039, 0.752941, 140.5099572962227, 0.865003,
                                        0.865003, 0.865003, 289.92859217707314, 0.705882, 0.0156863, 0.14902]
                    hLUT.ScalarRangeInitialized = 1.0

                        # show data in view
                    calculator2Display = Show(calculator2, renderView1)
                        # trace defaults for the display properties.
                    calculator2Display.ColorArrayName = ['POINTS', 'H']
                    calculator2Display.LookupTable = hLUT
                    calculator2Display.OSPRayScaleArray = 'H'
                    calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
                    calculator2Display.GlyphType = 'Arrow'
                    calculator2Display.ScalarOpacityUnitDistance = 0.003356151409034327
                    calculator2Display.SetScaleArray = ['POINTS', 'H']
                    calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
                    calculator2Display.OpacityArray = ['POINTS', 'H']
                    calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'

                        # hide data in view
                    Hide(gradientOfUnstructuredDataSet1, renderView1)

                        # show color bar/color legend
                    calculator2Display.SetScalarBarVisibility(renderView1, True)

                        # get opacity transfer function/opacity map for 'H'
                    hPWF = GetOpacityTransferFunction('H')
                    hPWF.Points = [-8.908677584627712, 0.0, 0.5, 0.0, 289.92859217707314, 1.0, 0.5, 0.0]
                    hPWF.ScalarRangeInitialized = 1

                        # hide data in view
                    Hide(calculator2, renderView1)

                        # set active source
                    SetActiveSource(gradientOfUnstructuredDataSet1)

                        # create a new 'Contour'
                    contour1 = Contour(Input=gradientOfUnstructuredDataSet1)
                    contour1.ContourBy = ['POINTS', 'Mx']
                    contour1.Isosurfaces = [-0.1503884196281433]
                    contour1.PointMergeMethod = 'Uniform Binning'

                        # set active source
                    SetActiveSource(gradientOfUnstructuredDataSet1)

                        # set active source
                    SetActiveSource(calculator2)

                        # create a new 'Calculator'
                    calculator3 = Calculator(Input=calculator2)
                    calculator3.Function = ''

                        # set active source
                    SetActiveSource(calculator2)

                        # create a new 'Contour'
                    contour1 = Contour(Input=calculator2)
                    contour1.ContourBy = ['POINTS', 'H']
                    contour1.Isosurfaces = [140.50995729622272]
                    contour1.PointMergeMethod = 'Uniform Binning'

                        # show data in view
                    contour1Display = Show(contour1, renderView1)
                        # trace defaults for the display properties.
                    contour1Display.ColorArrayName = [None, '']
                    contour1Display.OSPRayScaleArray = 'Gradients'
                    contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
                    contour1Display.GlyphType = 'Arrow'
                    contour1Display.SetScaleArray = ['POINTS', 'Mx']
                    contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
                    contour1Display.OpacityArray = ['POINTS', 'Mx']
                    contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

                        # hide data in view
                    Hide(calculator2, renderView1)

                        # set active source
                    SetActiveSource(calculator2)

                        # show data in view
                    calculator2Display = Show(calculator2, renderView1)

                        # show color bar/color legend
                    calculator2Display.SetScalarBarVisibility(renderView1, True)

                        # hide data in view
                    Hide(calculator2, renderView1)

                        # show color bar/color legend
                    calculator2Display.SetScalarBarVisibility(renderView1, True)

                        # hide color bar/color legend
                    calculator2Display.SetScalarBarVisibility(renderView1, False)

                        # set active source
                    SetActiveSource(contour1)

                        # change solid color
                    contour1Display.DiffuseColor = [0.0, 1.0, 0.0]

                        # current camera placement for renderView1
                    renderView1.CameraPosition = [0.05556550098723472, 0.017366116881115796,
                                                    0.04346285949267097]
                    renderView1.CameraFocalPoint = [-2.053845673799514e-05, 1.0849907994270245e-07,
                                                    -5.292261059553153e-21]
                    renderView1.CameraViewUp = [-0.11113589280628539, 0.963662653270126, -0.24290554547504817]
                    renderView1.CameraParallelScale = 0.018807449139699183

                        # EXPORT = os.path.splitext(FILE)[0][:-5]

                        # save screenshot
                        # name = EXPORT[:-3]

                        # try:
                        # int(EXPORT[-2])
                        # except:
                        # name = EXPORT[:-2]

                    new_dir = os.path.join(home,
                                            'plots',
                                            str(size))

                    if not os.path.isdir(new_dir):
                        os.mkdir(new_dir)

                    filename = os.path.splitext(FILE)[0][:-5]

                    finalpath = os.path.join(new_dir, filename + '.png')    
                            
                    if not os.path.exists(finalpath):
                        SaveScreenshot(finalpath, magnification=3, quality=100, view=renderView1)
                        i += 1
                        Disconnect()
                        Connect()
                  
                    






