__all__: list[str] = []

import cv2
import cv2.typing
import typing as _typing


RgbdNormals_RGBD_NORMALS_METHOD_FALS: int
RGBD_NORMALS_RGBD_NORMALS_METHOD_FALS: int
RgbdNormals_RGBD_NORMALS_METHOD_LINEMOD: int
RGBD_NORMALS_RGBD_NORMALS_METHOD_LINEMOD: int
RgbdNormals_RGBD_NORMALS_METHOD_SRI: int
RGBD_NORMALS_RGBD_NORMALS_METHOD_SRI: int
RgbdNormals_RGBD_NORMALS_METHOD = int
"""One of [RgbdNormals_RGBD_NORMALS_METHOD_FALS, RGBD_NORMALS_RGBD_NORMALS_METHOD_FALS, RgbdNormals_RGBD_NORMALS_METHOD_LINEMOD, RGBD_NORMALS_RGBD_NORMALS_METHOD_LINEMOD, RgbdNormals_RGBD_NORMALS_METHOD_SRI, RGBD_NORMALS_RGBD_NORMALS_METHOD_SRI]"""

DepthCleaner_DEPTH_CLEANER_NIL: int
DEPTH_CLEANER_DEPTH_CLEANER_NIL: int
DepthCleaner_DEPTH_CLEANER_METHOD = int
"""One of [DepthCleaner_DEPTH_CLEANER_NIL, DEPTH_CLEANER_DEPTH_CLEANER_NIL]"""

RgbdPlane_RGBD_PLANE_METHOD_DEFAULT: int
RGBD_PLANE_RGBD_PLANE_METHOD_DEFAULT: int
RgbdPlane_RGBD_PLANE_METHOD = int
"""One of [RgbdPlane_RGBD_PLANE_METHOD_DEFAULT, RGBD_PLANE_RGBD_PLANE_METHOD_DEFAULT]"""

OdometryFrame_CACHE_SRC: int
ODOMETRY_FRAME_CACHE_SRC: int
OdometryFrame_CACHE_DST: int
ODOMETRY_FRAME_CACHE_DST: int
OdometryFrame_CACHE_ALL: int
ODOMETRY_FRAME_CACHE_ALL: int

Odometry_ROTATION: int
ODOMETRY_ROTATION: int
Odometry_TRANSLATION: int
ODOMETRY_TRANSLATION: int
Odometry_RIGID_BODY_MOTION: int
ODOMETRY_RIGID_BODY_MOTION: int


# Classes
class RgbdNormals(cv2.Algorithm):
    # Functions
    @classmethod
    @_typing.overload
    def create(cls, rows: int, cols: int, depth: int, K: cv2.typing.MatLike, window_size: int = ..., method: int = ...) -> RgbdNormals: ...
    @classmethod
    @_typing.overload
    def create(cls, rows: int, cols: int, depth: int, K: cv2.UMat, window_size: int = ..., method: int = ...) -> RgbdNormals: ...

    @_typing.overload
    def apply(self, points: cv2.typing.MatLike, normals: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def apply(self, points: cv2.UMat, normals: cv2.UMat | None = ...) -> cv2.UMat: ...

    def initialize(self) -> None: ...

    def getRows(self) -> int: ...

    def setRows(self, val: int) -> None: ...

    def getCols(self) -> int: ...

    def setCols(self, val: int) -> None: ...

    def getWindowSize(self) -> int: ...

    def setWindowSize(self, val: int) -> None: ...

    def getDepth(self) -> int: ...

    def setDepth(self, val: int) -> None: ...

    def getK(self) -> cv2.typing.MatLike: ...

    def setK(self, val: cv2.typing.MatLike) -> None: ...

    def getMethod(self) -> int: ...

    def setMethod(self, val: int) -> None: ...


class DepthCleaner(cv2.Algorithm):
    # Functions
    @classmethod
    def create(cls, depth: int, window_size: int = ..., method: int = ...) -> DepthCleaner: ...

    @_typing.overload
    def apply(self, points: cv2.typing.MatLike, depth: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def apply(self, points: cv2.UMat, depth: cv2.UMat | None = ...) -> cv2.UMat: ...

    def initialize(self) -> None: ...

    def getWindowSize(self) -> int: ...

    def setWindowSize(self, val: int) -> None: ...

    def getDepth(self) -> int: ...

    def setDepth(self, val: int) -> None: ...

    def getMethod(self) -> int: ...

    def setMethod(self, val: int) -> None: ...


class RgbdPlane(cv2.Algorithm):
    # Functions
    @classmethod
    def create(cls, method: int, block_size: int, min_size: int, threshold: float, sensor_error_a: float = ..., sensor_error_b: float = ..., sensor_error_c: float = ...) -> RgbdPlane: ...

    @_typing.overload
    def apply(self, points3d: cv2.typing.MatLike, normals: cv2.typing.MatLike, mask: cv2.typing.MatLike | None = ..., plane_coefficients: cv2.typing.MatLike | None = ...) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @_typing.overload
    def apply(self, points3d: cv2.UMat, normals: cv2.UMat, mask: cv2.UMat | None = ..., plane_coefficients: cv2.UMat | None = ...) -> tuple[cv2.UMat, cv2.UMat]: ...
    @_typing.overload
    def apply(self, points3d: cv2.typing.MatLike, mask: cv2.typing.MatLike | None = ..., plane_coefficients: cv2.typing.MatLike | None = ...) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @_typing.overload
    def apply(self, points3d: cv2.UMat, mask: cv2.UMat | None = ..., plane_coefficients: cv2.UMat | None = ...) -> tuple[cv2.UMat, cv2.UMat]: ...

    def getBlockSize(self) -> int: ...

    def setBlockSize(self, val: int) -> None: ...

    def getMinSize(self) -> int: ...

    def setMinSize(self, val: int) -> None: ...

    def getMethod(self) -> int: ...

    def setMethod(self, val: int) -> None: ...

    def getThreshold(self) -> float: ...

    def setThreshold(self, val: float) -> None: ...

    def getSensorErrorA(self) -> float: ...

    def setSensorErrorA(self, val: float) -> None: ...

    def getSensorErrorB(self) -> float: ...

    def setSensorErrorB(self, val: float) -> None: ...

    def getSensorErrorC(self) -> float: ...

    def setSensorErrorC(self, val: float) -> None: ...


class RgbdFrame:
    @property
    def ID(self) -> int: ...
    @property
    def image(self) -> cv2.typing.MatLike: ...
    @property
    def depth(self) -> cv2.typing.MatLike: ...
    @property
    def mask(self) -> cv2.typing.MatLike: ...
    @property
    def normals(self) -> cv2.typing.MatLike: ...

    # Functions
    @classmethod
    def create(cls, image: cv2.typing.MatLike | None = ..., depth: cv2.typing.MatLike | None = ..., mask: cv2.typing.MatLike | None = ..., normals: cv2.typing.MatLike | None = ..., ID: int = ...) -> RgbdFrame: ...

    def release(self) -> None: ...


class OdometryFrame(RgbdFrame):
    @property
    def pyramidImage(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramidDepth(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramidMask(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramidCloud(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramid_dI_dx(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramid_dI_dy(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramidTexturedMask(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramidNormals(self) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @property
    def pyramidNormalsMask(self) -> _typing.Sequence[cv2.typing.MatLike]: ...

    # Functions
    @classmethod
    def create(cls, image: cv2.typing.MatLike | None = ..., depth: cv2.typing.MatLike | None = ..., mask: cv2.typing.MatLike | None = ..., normals: cv2.typing.MatLike | None = ..., ID: int = ...) -> OdometryFrame: ...

    def release(self) -> None: ...

    def releasePyramids(self) -> None: ...


class Odometry(cv2.Algorithm):
    # Functions
    def DEFAULT_MIN_DEPTH(self) -> float: ...

    def DEFAULT_MAX_DEPTH(self) -> float: ...

    def DEFAULT_MAX_DEPTH_DIFF(self) -> float: ...

    def DEFAULT_MAX_POINTS_PART(self) -> float: ...

    def DEFAULT_MAX_TRANSLATION(self) -> float: ...

    def DEFAULT_MAX_ROTATION(self) -> float: ...

    @_typing.overload
    def compute(self, srcImage: cv2.typing.MatLike, srcDepth: cv2.typing.MatLike, srcMask: cv2.typing.MatLike, dstImage: cv2.typing.MatLike, dstDepth: cv2.typing.MatLike, dstMask: cv2.typing.MatLike, Rt: cv2.typing.MatLike | None = ..., initRt: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.typing.MatLike]: ...
    @_typing.overload
    def compute(self, srcImage: cv2.typing.MatLike, srcDepth: cv2.typing.MatLike, srcMask: cv2.typing.MatLike, dstImage: cv2.typing.MatLike, dstDepth: cv2.typing.MatLike, dstMask: cv2.typing.MatLike, Rt: cv2.UMat | None = ..., initRt: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.UMat]: ...

    @_typing.overload
    def compute2(self, srcFrame: OdometryFrame, dstFrame: OdometryFrame, Rt: cv2.typing.MatLike | None = ..., initRt: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.typing.MatLike]: ...
    @_typing.overload
    def compute2(self, srcFrame: OdometryFrame, dstFrame: OdometryFrame, Rt: cv2.UMat | None = ..., initRt: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.UMat]: ...

    def prepareFrameCache(self, frame: OdometryFrame, cacheType: int) -> cv2.typing.Size: ...

    @classmethod
    def create(cls, odometryType: str) -> Odometry: ...

    def getCameraMatrix(self) -> cv2.typing.MatLike: ...

    def setCameraMatrix(self, val: cv2.typing.MatLike) -> None: ...

    def getTransformType(self) -> int: ...

    def setTransformType(self, val: int) -> None: ...


class RgbdOdometry(Odometry):
    # Functions
    @classmethod
    def create(cls, cameraMatrix: cv2.typing.MatLike | None = ..., minDepth: float = ..., maxDepth: float = ..., maxDepthDiff: float = ..., iterCounts: _typing.Sequence[int] = ..., minGradientMagnitudes: _typing.Sequence[float] = ..., maxPointsPart: float = ..., transformType: int = ...) -> RgbdOdometry: ...

    def prepareFrameCache(self, frame: OdometryFrame, cacheType: int) -> cv2.typing.Size: ...

    def getCameraMatrix(self) -> cv2.typing.MatLike: ...

    def setCameraMatrix(self, val: cv2.typing.MatLike) -> None: ...

    def getMinDepth(self) -> float: ...

    def setMinDepth(self, val: float) -> None: ...

    def getMaxDepth(self) -> float: ...

    def setMaxDepth(self, val: float) -> None: ...

    def getMaxDepthDiff(self) -> float: ...

    def setMaxDepthDiff(self, val: float) -> None: ...

    def getIterationCounts(self) -> cv2.typing.MatLike: ...

    def setIterationCounts(self, val: cv2.typing.MatLike) -> None: ...

    def getMinGradientMagnitudes(self) -> cv2.typing.MatLike: ...

    def setMinGradientMagnitudes(self, val: cv2.typing.MatLike) -> None: ...

    def getMaxPointsPart(self) -> float: ...

    def setMaxPointsPart(self, val: float) -> None: ...

    def getTransformType(self) -> int: ...

    def setTransformType(self, val: int) -> None: ...

    def getMaxTranslation(self) -> float: ...

    def setMaxTranslation(self, val: float) -> None: ...

    def getMaxRotation(self) -> float: ...

    def setMaxRotation(self, val: float) -> None: ...


class ICPOdometry(Odometry):
    # Functions
    @classmethod
    def create(cls, cameraMatrix: cv2.typing.MatLike | None = ..., minDepth: float = ..., maxDepth: float = ..., maxDepthDiff: float = ..., maxPointsPart: float = ..., iterCounts: _typing.Sequence[int] = ..., transformType: int = ...) -> ICPOdometry: ...

    def prepareFrameCache(self, frame: OdometryFrame, cacheType: int) -> cv2.typing.Size: ...

    def getCameraMatrix(self) -> cv2.typing.MatLike: ...

    def setCameraMatrix(self, val: cv2.typing.MatLike) -> None: ...

    def getMinDepth(self) -> float: ...

    def setMinDepth(self, val: float) -> None: ...

    def getMaxDepth(self) -> float: ...

    def setMaxDepth(self, val: float) -> None: ...

    def getMaxDepthDiff(self) -> float: ...

    def setMaxDepthDiff(self, val: float) -> None: ...

    def getIterationCounts(self) -> cv2.typing.MatLike: ...

    def setIterationCounts(self, val: cv2.typing.MatLike) -> None: ...

    def getMaxPointsPart(self) -> float: ...

    def setMaxPointsPart(self, val: float) -> None: ...

    def getTransformType(self) -> int: ...

    def setTransformType(self, val: int) -> None: ...

    def getMaxTranslation(self) -> float: ...

    def setMaxTranslation(self, val: float) -> None: ...

    def getMaxRotation(self) -> float: ...

    def setMaxRotation(self, val: float) -> None: ...

    def getNormalsComputer(self) -> RgbdNormals: ...


class RgbdICPOdometry(Odometry):
    # Functions
    @classmethod
    def create(cls, cameraMatrix: cv2.typing.MatLike | None = ..., minDepth: float = ..., maxDepth: float = ..., maxDepthDiff: float = ..., maxPointsPart: float = ..., iterCounts: _typing.Sequence[int] = ..., minGradientMagnitudes: _typing.Sequence[float] = ..., transformType: int = ...) -> RgbdICPOdometry: ...

    def prepareFrameCache(self, frame: OdometryFrame, cacheType: int) -> cv2.typing.Size: ...

    def getCameraMatrix(self) -> cv2.typing.MatLike: ...

    def setCameraMatrix(self, val: cv2.typing.MatLike) -> None: ...

    def getMinDepth(self) -> float: ...

    def setMinDepth(self, val: float) -> None: ...

    def getMaxDepth(self) -> float: ...

    def setMaxDepth(self, val: float) -> None: ...

    def getMaxDepthDiff(self) -> float: ...

    def setMaxDepthDiff(self, val: float) -> None: ...

    def getMaxPointsPart(self) -> float: ...

    def setMaxPointsPart(self, val: float) -> None: ...

    def getIterationCounts(self) -> cv2.typing.MatLike: ...

    def setIterationCounts(self, val: cv2.typing.MatLike) -> None: ...

    def getMinGradientMagnitudes(self) -> cv2.typing.MatLike: ...

    def setMinGradientMagnitudes(self, val: cv2.typing.MatLike) -> None: ...

    def getTransformType(self) -> int: ...

    def setTransformType(self, val: int) -> None: ...

    def getMaxTranslation(self) -> float: ...

    def setMaxTranslation(self, val: float) -> None: ...

    def getMaxRotation(self) -> float: ...

    def setMaxRotation(self, val: float) -> None: ...

    def getNormalsComputer(self) -> RgbdNormals: ...


class FastICPOdometry(Odometry):
    # Functions
    @classmethod
    def create(cls, cameraMatrix: cv2.typing.MatLike, maxDistDiff: float = ..., angleThreshold: float = ..., sigmaDepth: float = ..., sigmaSpatial: float = ..., kernelSize: int = ..., iterCounts: _typing.Sequence[int] = ...) -> FastICPOdometry: ...

    def prepareFrameCache(self, frame: OdometryFrame, cacheType: int) -> cv2.typing.Size: ...

    def getCameraMatrix(self) -> cv2.typing.MatLike: ...

    def setCameraMatrix(self, val: cv2.typing.MatLike) -> None: ...

    def getMaxDistDiff(self) -> float: ...

    def setMaxDistDiff(self, val: float) -> None: ...

    def getAngleThreshold(self) -> float: ...

    def setAngleThreshold(self, f: float) -> None: ...

    def getSigmaDepth(self) -> float: ...

    def setSigmaDepth(self, f: float) -> None: ...

    def getSigmaSpatial(self) -> float: ...

    def setSigmaSpatial(self, f: float) -> None: ...

    def getKernelSize(self) -> int: ...

    def setKernelSize(self, f: int) -> None: ...

    def getIterationCounts(self) -> cv2.typing.MatLike: ...

    def setIterationCounts(self, val: cv2.typing.MatLike) -> None: ...

    def getTransformType(self) -> int: ...

    def setTransformType(self, val: int) -> None: ...



# Functions
@_typing.overload
def depthTo3d(depth: cv2.typing.MatLike, K: cv2.typing.MatLike, points3d: cv2.typing.MatLike | None = ..., mask: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def depthTo3d(depth: cv2.UMat, K: cv2.UMat, points3d: cv2.UMat | None = ..., mask: cv2.UMat | None = ...) -> cv2.UMat: ...

@_typing.overload
def depthTo3dSparse(depth: cv2.typing.MatLike, in_K: cv2.typing.MatLike, in_points: cv2.typing.MatLike, points3d: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def depthTo3dSparse(depth: cv2.UMat, in_K: cv2.UMat, in_points: cv2.UMat, points3d: cv2.UMat | None = ...) -> cv2.UMat: ...

@_typing.overload
def registerDepth(unregisteredCameraMatrix: cv2.typing.MatLike, registeredCameraMatrix: cv2.typing.MatLike, registeredDistCoeffs: cv2.typing.MatLike, Rt: cv2.typing.MatLike, unregisteredDepth: cv2.typing.MatLike, outputImagePlaneSize: cv2.typing.Size, registeredDepth: cv2.typing.MatLike | None = ..., depthDilation: bool = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def registerDepth(unregisteredCameraMatrix: cv2.UMat, registeredCameraMatrix: cv2.UMat, registeredDistCoeffs: cv2.UMat, Rt: cv2.UMat, unregisteredDepth: cv2.UMat, outputImagePlaneSize: cv2.typing.Size, registeredDepth: cv2.UMat | None = ..., depthDilation: bool = ...) -> cv2.UMat: ...

@_typing.overload
def rescaleDepth(in_: cv2.typing.MatLike, depth: int, out: cv2.typing.MatLike | None = ..., depth_factor: float = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def rescaleDepth(in_: cv2.UMat, depth: int, out: cv2.UMat | None = ..., depth_factor: float = ...) -> cv2.UMat: ...

@_typing.overload
def warpFrame(image: cv2.typing.MatLike, depth: cv2.typing.MatLike, mask: cv2.typing.MatLike, Rt: cv2.typing.MatLike, cameraMatrix: cv2.typing.MatLike, distCoeff: cv2.typing.MatLike, warpedImage: cv2.typing.MatLike | None = ..., warpedDepth: cv2.typing.MatLike | None = ..., warpedMask: cv2.typing.MatLike | None = ...) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]: ...
@_typing.overload
def warpFrame(image: cv2.typing.MatLike, depth: cv2.typing.MatLike, mask: cv2.typing.MatLike, Rt: cv2.typing.MatLike, cameraMatrix: cv2.typing.MatLike, distCoeff: cv2.typing.MatLike, warpedImage: cv2.UMat | None = ..., warpedDepth: cv2.UMat | None = ..., warpedMask: cv2.UMat | None = ...) -> tuple[cv2.UMat, cv2.UMat, cv2.UMat]: ...


