from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingCore

class vtkHyperTreeGridMapper(vtkmodules.vtkRenderingCore.vtkMapper):
    def FillInputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds:MutableSequence[float]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetUseAdaptiveDecimation(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkHyperTreeGridMapper': ...
    def Render(self, ren:'vtkRenderer', act:'vtkActor') -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkHyperTreeGridMapper': ...
    @overload
    def SetInputConnection(self, port:int, input:'vtkAlgorithmOutput') -> None: ...
    @overload
    def SetInputConnection(self, input:'vtkAlgorithmOutput') -> None: ...
    @overload
    def SetInputDataObject(self, port:int, input:'vtkDataObject') -> None: ...
    @overload
    def SetInputDataObject(self, input:'vtkDataObject') -> None: ...
    def SetUseAdaptiveDecimation(self, _arg:bool) -> None: ...
    def UseAdaptiveDecimationOff(self) -> None: ...
    def UseAdaptiveDecimationOn(self) -> None: ...
