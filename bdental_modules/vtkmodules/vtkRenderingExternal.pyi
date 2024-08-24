from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingOpenGL2

class ExternalVTKWidget(vtkmodules.vtkCommonCore.vtkObject):
    def AddRenderer(self) -> 'vtkExternalOpenGLRenderer': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetRenderWindow(self) -> 'vtkExternalOpenGLRenderWindow': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'ExternalVTKWidget': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'ExternalVTKWidget': ...
    def SetRenderWindow(self, renWin:'vtkExternalOpenGLRenderWindow') -> None: ...

class vtkExternalLight(vtkmodules.vtkRenderingCore.vtkLight):
    class ReplaceModes(int): ...
    ALL_PARAMS:'ReplaceModes'
    INDIVIDUAL_PARAMS:'ReplaceModes'
    def GetAmbientColorSet(self) -> bool: ...
    def GetAttenuationValuesSet(self) -> bool: ...
    def GetConeAngleSet(self) -> bool: ...
    def GetDiffuseColorSet(self) -> bool: ...
    def GetExponentSet(self) -> bool: ...
    def GetFocalPointSet(self) -> bool: ...
    def GetIntensitySet(self) -> bool: ...
    def GetLightIndex(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPositionSet(self) -> bool: ...
    def GetPositionalSet(self) -> bool: ...
    def GetReplaceMode(self) -> int: ...
    def GetSpecularColorSet(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExternalLight': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExternalLight': ...
    @overload
    def SetAmbientColor(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetAmbientColor(self, _arg:Sequence[float]) -> None: ...
    @overload
    def SetAttenuationValues(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetAttenuationValues(self, _arg:Sequence[float]) -> None: ...
    def SetConeAngle(self, __a:float) -> None: ...
    @overload
    def SetDiffuseColor(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetDiffuseColor(self, _arg:Sequence[float]) -> None: ...
    def SetExponent(self, __a:float) -> None: ...
    @overload
    def SetFocalPoint(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetFocalPoint(self, _arg:Sequence[float]) -> None: ...
    def SetIntensity(self, __a:float) -> None: ...
    def SetLightIndex(self, _arg:int) -> None: ...
    @overload
    def SetPosition(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetPosition(self, _arg:Sequence[float]) -> None: ...
    def SetPositional(self, __a:int) -> None: ...
    def SetReplaceMode(self, _arg:int) -> None: ...
    @overload
    def SetSpecularColor(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetSpecularColor(self, _arg:Sequence[float]) -> None: ...

class vtkExternalOpenGLCamera(vtkmodules.vtkRenderingOpenGL2.vtkOpenGLCamera):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExternalOpenGLCamera': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExternalOpenGLCamera': ...
    def SetProjectionTransformMatrix(self, elements:Sequence[float]) -> None: ...
    def SetViewTransformMatrix(self, elements:Sequence[float]) -> None: ...

class vtkExternalOpenGLRenderWindow(vtkmodules.vtkRenderingOpenGL2.vtkGenericOpenGLRenderWindow):
    def AutomaticWindowPositionAndResizeOff(self) -> None: ...
    def AutomaticWindowPositionAndResizeOn(self) -> None: ...
    def GetAutomaticWindowPositionAndResize(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetUseExternalContent(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    def IsCurrent(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExternalOpenGLRenderWindow': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExternalOpenGLRenderWindow': ...
    def SetAutomaticWindowPositionAndResize(self, _arg:int) -> None: ...
    def SetUseExternalContent(self, _arg:bool) -> None: ...
    def Start(self) -> None: ...
    def UseExternalContentOff(self) -> None: ...
    def UseExternalContentOn(self) -> None: ...

class vtkExternalOpenGLRenderer(vtkmodules.vtkRenderingOpenGL2.vtkOpenGLRenderer):
    def AddExternalLight(self, __a:'vtkExternalLight') -> None: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPreserveGLCameraMatrices(self) -> int: ...
    def GetPreserveGLLights(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def MakeCamera(self) -> 'vtkCamera': ...
    def NewInstance(self) -> 'vtkExternalOpenGLRenderer': ...
    def PreserveGLCameraMatricesOff(self) -> None: ...
    def PreserveGLCameraMatricesOn(self) -> None: ...
    def PreserveGLLightsOff(self) -> None: ...
    def PreserveGLLightsOn(self) -> None: ...
    def RemoveAllExternalLights(self) -> None: ...
    def RemoveExternalLight(self, __a:'vtkExternalLight') -> None: ...
    def Render(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExternalOpenGLRenderer': ...
    def SetPreserveGLCameraMatrices(self, _arg:int) -> None: ...
    def SetPreserveGLLights(self, _arg:int) -> None: ...

