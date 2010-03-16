# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_PreludeEasy', [dirname(__file__)])
        except ImportError:
            import _PreludeEasy
            return _PreludeEasy
        if fp is not None:
            try:
                _mod = imp.load_module('_PreludeEasy', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _PreludeEasy = swig_import_helper()
    del swig_import_helper
else:
    import _PreludeEasy
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _PreludeEasy.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _PreludeEasy.SwigPyIterator_value(self)
    def incr(self, n = 1): return _PreludeEasy.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _PreludeEasy.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _PreludeEasy.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _PreludeEasy.SwigPyIterator_equal(self, *args)
    def copy(self): return _PreludeEasy.SwigPyIterator_copy(self)
    def next(self): return _PreludeEasy.SwigPyIterator_next(self)
    def __next__(self): return _PreludeEasy.SwigPyIterator___next__(self)
    def previous(self): return _PreludeEasy.SwigPyIterator_previous(self)
    def advance(self, *args): return _PreludeEasy.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _PreludeEasy.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _PreludeEasy.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _PreludeEasy.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _PreludeEasy.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _PreludeEasy.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _PreludeEasy.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _PreludeEasy.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class PreludeLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PreludeLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PreludeLog, name)
    __repr__ = _swig_repr
    DEBUG = _PreludeEasy.PreludeLog_DEBUG
    INFO = _PreludeEasy.PreludeLog_INFO
    WARNING = _PreludeEasy.PreludeLog_WARNING
    ERROR = _PreludeEasy.PreludeLog_ERROR
    CRITICAL = _PreludeEasy.PreludeLog_CRITICAL
    QUIET = _PreludeEasy.PreludeLog_QUIET
    SYSLOG = _PreludeEasy.PreludeLog_SYSLOG
    __swig_getmethods__["SetLevel"] = lambda x: _PreludeEasy.PreludeLog_SetLevel
    if _newclass:SetLevel = staticmethod(_PreludeEasy.PreludeLog_SetLevel)
    __swig_getmethods__["SetDebugLevel"] = lambda x: _PreludeEasy.PreludeLog_SetDebugLevel
    if _newclass:SetDebugLevel = staticmethod(_PreludeEasy.PreludeLog_SetDebugLevel)
    __swig_getmethods__["SetFlags"] = lambda x: _PreludeEasy.PreludeLog_SetFlags
    if _newclass:SetFlags = staticmethod(_PreludeEasy.PreludeLog_SetFlags)
    __swig_getmethods__["GetFlags"] = lambda x: _PreludeEasy.PreludeLog_GetFlags
    if _newclass:GetFlags = staticmethod(_PreludeEasy.PreludeLog_GetFlags)
    __swig_getmethods__["SetLogfile"] = lambda x: _PreludeEasy.PreludeLog_SetLogfile
    if _newclass:SetLogfile = staticmethod(_PreludeEasy.PreludeLog_SetLogfile)
    __swig_getmethods__["SetCallback"] = lambda x: _PreludeEasy.PreludeLog_SetCallback
    if _newclass:SetCallback = staticmethod(_PreludeEasy.PreludeLog_SetCallback)
    def __init__(self): 
        this = _PreludeEasy.new_PreludeLog()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PreludeEasy.delete_PreludeLog
    __del__ = lambda self : None;
PreludeLog_swigregister = _PreludeEasy.PreludeLog_swigregister
PreludeLog_swigregister(PreludeLog)

def CheckVersion(version = None):
  return _PreludeEasy.CheckVersion(version)
CheckVersion = _PreludeEasy.CheckVersion

def PreludeLog_SetLevel(*args):
  return _PreludeEasy.PreludeLog_SetLevel(*args)
PreludeLog_SetLevel = _PreludeEasy.PreludeLog_SetLevel

def PreludeLog_SetDebugLevel(*args):
  return _PreludeEasy.PreludeLog_SetDebugLevel(*args)
PreludeLog_SetDebugLevel = _PreludeEasy.PreludeLog_SetDebugLevel

def PreludeLog_SetFlags(*args):
  return _PreludeEasy.PreludeLog_SetFlags(*args)
PreludeLog_SetFlags = _PreludeEasy.PreludeLog_SetFlags

def PreludeLog_GetFlags():
  return _PreludeEasy.PreludeLog_GetFlags()
PreludeLog_GetFlags = _PreludeEasy.PreludeLog_GetFlags

def PreludeLog_SetLogfile(*args):
  return _PreludeEasy.PreludeLog_SetLogfile(*args)
PreludeLog_SetLogfile = _PreludeEasy.PreludeLog_SetLogfile

def PreludeLog_SetCallback(*args):
  return _PreludeEasy.PreludeLog_SetCallback(*args)
PreludeLog_SetCallback = _PreludeEasy.PreludeLog_SetCallback

class PreludeError(Exception):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PreludeError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PreludeError, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _PreludeEasy.delete_PreludeError
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_PreludeError(*args)
        try: self.this.append(this)
        except: self.this = this
    def what(self): return _PreludeEasy.PreludeError_what(self)
    def __str__(self): return _PreludeEasy.PreludeError___str__(self)
PreludeError_swigregister = _PreludeEasy.PreludeError_swigregister
PreludeError_swigregister(PreludeError)

class Connection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Connection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Connection, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _PreludeEasy.delete_Connection
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_Connection(*args)
        try: self.this.append(this)
        except: self.this = this
    def GetConnection(self): return _PreludeEasy.Connection_GetConnection(self)
    def Close(self): return _PreludeEasy.Connection_Close(self)
    def Connect(self, *args): return _PreludeEasy.Connection_Connect(self, *args)
    def SetState(self, *args): return _PreludeEasy.Connection_SetState(self, *args)
    def GetState(self): return _PreludeEasy.Connection_GetState(self)
    def SetData(self, *args): return _PreludeEasy.Connection_SetData(self, *args)
    def GetData(self): return _PreludeEasy.Connection_GetData(self)
    def GetPermission(self): return _PreludeEasy.Connection_GetPermission(self)
    def SetPeerAnalyzerid(self, *args): return _PreludeEasy.Connection_SetPeerAnalyzerid(self, *args)
    def GetPeerAnalyzerid(self): return _PreludeEasy.Connection_GetPeerAnalyzerid(self)
    def GetLocalAddr(self): return _PreludeEasy.Connection_GetLocalAddr(self)
    def GetLocalPort(self): return _PreludeEasy.Connection_GetLocalPort(self)
    def GetPeerAddr(self): return _PreludeEasy.Connection_GetPeerAddr(self)
    def GetPeerPort(self): return _PreludeEasy.Connection_GetPeerPort(self)
    def IsAlive(self): return _PreludeEasy.Connection_IsAlive(self)
    def GetFd(self): return _PreludeEasy.Connection_GetFd(self)
    def RecvIDMEF(self): return _PreludeEasy.Connection_RecvIDMEF(self)
Connection_swigregister = _PreludeEasy.Connection_swigregister
Connection_swigregister(Connection)

class ConnectionPool(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConnectionPool, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ConnectionPool, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _PreludeEasy.delete_ConnectionPool
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_ConnectionPool(*args)
        try: self.this.append(this)
        except: self.this = this
    def Init(self): return _PreludeEasy.ConnectionPool_Init(self)
    def SetConnectionString(self, *args): return _PreludeEasy.ConnectionPool_SetConnectionString(self, *args)
    def GetConnectionString(self): return _PreludeEasy.ConnectionPool_GetConnectionString(self)
    def GetConnectionList(self): return _PreludeEasy.ConnectionPool_GetConnectionList(self)
    def SetFlags(self, *args): return _PreludeEasy.ConnectionPool_SetFlags(self, *args)
    def GetFlags(self): return _PreludeEasy.ConnectionPool_GetFlags(self)
    def SetData(self, *args): return _PreludeEasy.ConnectionPool_SetData(self, *args)
    def GetData(self): return _PreludeEasy.ConnectionPool_GetData(self)
    def AddConnection(self, *args): return _PreludeEasy.ConnectionPool_AddConnection(self, *args)
    def DelConnection(self, *args): return _PreludeEasy.ConnectionPool_DelConnection(self, *args)
    def SetConnectionAlive(self, *args): return _PreludeEasy.ConnectionPool_SetConnectionAlive(self, *args)
    def SetConnectionDead(self, *args): return _PreludeEasy.ConnectionPool_SetConnectionDead(self, *args)
    def SetRequiredPermission(self, *args): return _PreludeEasy.ConnectionPool_SetRequiredPermission(self, *args)
ConnectionPool_swigregister = _PreludeEasy.ConnectionPool_swigregister
ConnectionPool_swigregister(ConnectionPool)

class ClientProfile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ClientProfile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ClientProfile, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _PreludeEasy.new_ClientProfile(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PreludeEasy.delete_ClientProfile
    __del__ = lambda self : None;
    def GetUid(self): return _PreludeEasy.ClientProfile_GetUid(self)
    def GetGid(self): return _PreludeEasy.ClientProfile_GetGid(self)
    def GetName(self): return _PreludeEasy.ClientProfile_GetName(self)
    def SetName(self, *args): return _PreludeEasy.ClientProfile_SetName(self, *args)
    def GetAnalyzerId(self, *args): return _PreludeEasy.ClientProfile_GetAnalyzerId(self, *args)
    def GetConfigFilename(self): return _PreludeEasy.ClientProfile_GetConfigFilename(self)
    def GetAnalyzeridFilename(self): return _PreludeEasy.ClientProfile_GetAnalyzeridFilename(self)
    def GetTlsKeyFilename(self): return _PreludeEasy.ClientProfile_GetTlsKeyFilename(self)
    def GetTlsServerCaCertFilename(self): return _PreludeEasy.ClientProfile_GetTlsServerCaCertFilename(self)
    def GetTlsServerKeyCertFilename(self): return _PreludeEasy.ClientProfile_GetTlsServerKeyCertFilename(self)
    def GetTlsServerCrlFilename(self): return _PreludeEasy.ClientProfile_GetTlsServerCrlFilename(self)
    def GetTlsClientKeyCertFilename(self): return _PreludeEasy.ClientProfile_GetTlsClientKeyCertFilename(self)
    def GetTlsClientTrustedCertFilename(self): return _PreludeEasy.ClientProfile_GetTlsClientTrustedCertFilename(self)
    def GetBackupDirname(self): return _PreludeEasy.ClientProfile_GetBackupDirname(self)
    def GetProfileDirname(self): return _PreludeEasy.ClientProfile_GetProfileDirname(self)
    def SetPrefix(self, *args): return _PreludeEasy.ClientProfile_SetPrefix(self, *args)
    def GetPrefix(self): return _PreludeEasy.ClientProfile_GetPrefix(self)
ClientProfile_swigregister = _PreludeEasy.ClientProfile_swigregister
ClientProfile_swigregister(ClientProfile)

class Client(ClientProfile):
    __swig_setmethods__ = {}
    for _s in [ClientProfile]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Client, name, value)
    __swig_getmethods__ = {}
    for _s in [ClientProfile]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Client, name)
    __repr__ = _swig_repr
    ASYNC_SEND = _PreludeEasy.Client_ASYNC_SEND
    FLAGS_ASYNC_SEND = _PreludeEasy.Client_FLAGS_ASYNC_SEND
    ASYNC_TIMER = _PreludeEasy.Client_ASYNC_TIMER
    FLAGS_ASYNC_TIMER = _PreludeEasy.Client_FLAGS_ASYNC_TIMER
    HEARTBEAT = _PreludeEasy.Client_HEARTBEAT
    FLAGS_HEARTBEAT = _PreludeEasy.Client_FLAGS_HEARTBEAT
    CONNECT = _PreludeEasy.Client_CONNECT
    FLAGS_CONNECT = _PreludeEasy.Client_FLAGS_CONNECT
    AUTOCONFIG = _PreludeEasy.Client_AUTOCONFIG
    FLAGS_AUTOCONFIG = _PreludeEasy.Client_FLAGS_AUTOCONFIG
    IDMEF_READ = _PreludeEasy.Client_IDMEF_READ
    PERMISSION_IDMEF_READ = _PreludeEasy.Client_PERMISSION_IDMEF_READ
    ADMIN_READ = _PreludeEasy.Client_ADMIN_READ
    PERMISSION_ADMIN_READ = _PreludeEasy.Client_PERMISSION_ADMIN_READ
    IDMEF_WRITE = _PreludeEasy.Client_IDMEF_WRITE
    PERMISSION_IDMEF_WRITE = _PreludeEasy.Client_PERMISSION_IDMEF_WRITE
    ADMIN_WRITE = _PreludeEasy.Client_ADMIN_WRITE
    PERMISSION_ADMIN_WRITE = _PreludeEasy.Client_PERMISSION_ADMIN_WRITE
    __swig_destroy__ = _PreludeEasy.delete_Client
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_Client(*args)
        try: self.this.append(this)
        except: self.this = this
    def Start(self): return _PreludeEasy.Client_Start(self)
    def Init(self): return _PreludeEasy.Client_Init(self)
    def GetClient(self): return _PreludeEasy.Client_GetClient(self)
    def SendIDMEF(self, *args): return _PreludeEasy.Client_SendIDMEF(self, *args)
    def RecvIDMEF(self, *args): return _PreludeEasy.Client_RecvIDMEF(self, *args)
    def GetFlags(self): return _PreludeEasy.Client_GetFlags(self)
    def SetFlags(self, *args): return _PreludeEasy.Client_SetFlags(self, *args)
    def GetRequiredPermission(self): return _PreludeEasy.Client_GetRequiredPermission(self)
    def SetRequiredPermission(self, *args): return _PreludeEasy.Client_SetRequiredPermission(self, *args)
    def GetConfigFilename(self): return _PreludeEasy.Client_GetConfigFilename(self)
    def SetConfigFilename(self, *args): return _PreludeEasy.Client_SetConfigFilename(self, *args)
    def GetConnectionPool(self): return _PreludeEasy.Client_GetConnectionPool(self)
    def SetConnectionPool(self, *args): return _PreludeEasy.Client_SetConnectionPool(self, *args)
    def __lshift__(self, *args): return _PreludeEasy.Client___lshift__(self, *args)
    def __rshift__(self, *args): return _PreludeEasy.Client___rshift__(self, *args)
    __swig_getmethods__["SetRecvTimeout"] = lambda x: _PreludeEasy.Client_SetRecvTimeout
    if _newclass:SetRecvTimeout = staticmethod(_PreludeEasy.Client_SetRecvTimeout)
Client_swigregister = _PreludeEasy.Client_swigregister
Client_swigregister(Client)

def Client_SetRecvTimeout(*args):
  return _PreludeEasy.Client_SetRecvTimeout(*args)
Client_SetRecvTimeout = _PreludeEasy.Client_SetRecvTimeout

class ClientEasy(Client):
    __swig_setmethods__ = {}
    for _s in [Client]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ClientEasy, name, value)
    __swig_getmethods__ = {}
    for _s in [Client]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ClientEasy, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _PreludeEasy.new_ClientEasy(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PreludeEasy.delete_ClientEasy
    __del__ = lambda self : None;
ClientEasy_swigregister = _PreludeEasy.ClientEasy_swigregister
ClientEasy_swigregister(ClientEasy)

class IDMEFCriterion(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDMEFCriterion, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDMEFCriterion, name)
    __repr__ = _swig_repr
    OPERATOR_NOT = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT
    OPERATOR_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_NOCASE
    OPERATOR_EQUAL = _PreludeEasy.IDMEFCriterion_OPERATOR_EQUAL
    OPERATOR_EQUAL_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_EQUAL_NOCASE
    OPERATOR_NOT_EQUAL = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_EQUAL
    OPERATOR_NOT_EQUAL_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_EQUAL_NOCASE
    OPERATOR_LESSER = _PreludeEasy.IDMEFCriterion_OPERATOR_LESSER
    OPERATOR_LESSER_OR_EQUAL = _PreludeEasy.IDMEFCriterion_OPERATOR_LESSER_OR_EQUAL
    OPERATOR_GREATER = _PreludeEasy.IDMEFCriterion_OPERATOR_GREATER
    OPERATOR_GREATER_OR_EQUAL = _PreludeEasy.IDMEFCriterion_OPERATOR_GREATER_OR_EQUAL
    OPERATOR_SUBSTR = _PreludeEasy.IDMEFCriterion_OPERATOR_SUBSTR
    OPERATOR_SUBSTR_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_SUBSTR_NOCASE
    OPERATOR_NOT_SUBSTR = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_SUBSTR
    OPERATOR_NOT_SUBSTR_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_SUBSTR_NOCASE
    OPERATOR_REGEX = _PreludeEasy.IDMEFCriterion_OPERATOR_REGEX
    OPERATOR_REGEX_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_REGEX_NOCASE
    OPERATOR_NOT_REGEX = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_REGEX
    OPERATOR_NOT_REGEX_NOCASE = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_REGEX_NOCASE
    OPERATOR_NULL = _PreludeEasy.IDMEFCriterion_OPERATOR_NULL
    OPERATOR_NOT_NULL = _PreludeEasy.IDMEFCriterion_OPERATOR_NOT_NULL
    def __init__(self): 
        this = _PreludeEasy.new_IDMEFCriterion()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PreludeEasy.delete_IDMEFCriterion
    __del__ = lambda self : None;
IDMEFCriterion_swigregister = _PreludeEasy.IDMEFCriterion_swigregister
IDMEFCriterion_swigregister(IDMEFCriterion)

class IDMEFCriteria(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDMEFCriteria, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDMEFCriteria, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _PreludeEasy.delete_IDMEFCriteria
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_IDMEFCriteria(*args)
        try: self.this.append(this)
        except: self.this = this
    def Match(self, *args): return _PreludeEasy.IDMEFCriteria_Match(self, *args)
    def Clone(self): return _PreludeEasy.IDMEFCriteria_Clone(self)
    def ANDCriteria(self, *args): return _PreludeEasy.IDMEFCriteria_ANDCriteria(self, *args)
    def ORCriteria(self, *args): return _PreludeEasy.IDMEFCriteria_ORCriteria(self, *args)
    def ToString(self): return _PreludeEasy.IDMEFCriteria_ToString(self)
    def __str__(self): return _PreludeEasy.IDMEFCriteria___str__(self)
IDMEFCriteria_swigregister = _PreludeEasy.IDMEFCriteria_swigregister
IDMEFCriteria_swigregister(IDMEFCriteria)

class IDMEFValue(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDMEFValue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDMEFValue, name)
    __repr__ = _swig_repr
    def GetType(self): return _PreludeEasy.IDMEFValue_GetType(self)
    def IsNull(self): return _PreludeEasy.IDMEFValue_IsNull(self)
    __swig_destroy__ = _PreludeEasy.delete_IDMEFValue
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_IDMEFValue(*args)
        try: self.this.append(this)
        except: self.this = this
    def Match(self, *args): return _PreludeEasy.IDMEFValue_Match(self, *args)
    def Clone(self): return _PreludeEasy.IDMEFValue_Clone(self)
IDMEFValue_swigregister = _PreludeEasy.IDMEFValue_swigregister
IDMEFValue_swigregister(IDMEFValue)

class IDMEFPath(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDMEFPath, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDMEFPath, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _PreludeEasy.new_IDMEFPath(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PreludeEasy.delete_IDMEFPath
    __del__ = lambda self : None;
    def Get(self, *args): return _PreludeEasy.IDMEFPath_Get(self, *args)
    def Set(self, *args): return _PreludeEasy.IDMEFPath_Set(self, *args)
    def GetClass(self, *args): return _PreludeEasy.IDMEFPath_GetClass(self, *args)
    def GetValueType(self, *args): return _PreludeEasy.IDMEFPath_GetValueType(self, *args)
    def SetIndex(self, *args): return _PreludeEasy.IDMEFPath_SetIndex(self, *args)
    def UndefineIndex(self, *args): return _PreludeEasy.IDMEFPath_UndefineIndex(self, *args)
    def GetIndex(self, *args): return _PreludeEasy.IDMEFPath_GetIndex(self, *args)
    def MakeChild(self, *args): return _PreludeEasy.IDMEFPath_MakeChild(self, *args)
    def MakeParent(self): return _PreludeEasy.IDMEFPath_MakeParent(self)
    def Compare(self, *args): return _PreludeEasy.IDMEFPath_Compare(self, *args)
    def Clone(self): return _PreludeEasy.IDMEFPath_Clone(self)
    def CheckOperator(self, *args): return _PreludeEasy.IDMEFPath_CheckOperator(self, *args)
    def GetApplicableOperators(self): return _PreludeEasy.IDMEFPath_GetApplicableOperators(self)
    def GetName(self, *args): return _PreludeEasy.IDMEFPath_GetName(self, *args)
    def IsAmbiguous(self): return _PreludeEasy.IDMEFPath_IsAmbiguous(self)
    def HasLists(self): return _PreludeEasy.IDMEFPath_HasLists(self)
    def IsList(self, *args): return _PreludeEasy.IDMEFPath_IsList(self, *args)
    def GetDepth(self): return _PreludeEasy.IDMEFPath_GetDepth(self)
IDMEFPath_swigregister = _PreludeEasy.IDMEFPath_swigregister
IDMEFPath_swigregister(IDMEFPath)

class IDMEFTime(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDMEFTime, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDMEFTime, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _PreludeEasy.new_IDMEFTime(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PreludeEasy.delete_IDMEFTime
    __del__ = lambda self : None;
    def Set(self, *args): return _PreludeEasy.IDMEFTime_Set(self, *args)
    def SetSec(self, *args): return _PreludeEasy.IDMEFTime_SetSec(self, *args)
    def SetUSec(self, *args): return _PreludeEasy.IDMEFTime_SetUSec(self, *args)
    def SetGmtOffset(self, *args): return _PreludeEasy.IDMEFTime_SetGmtOffset(self, *args)
    def GetSec(self): return _PreludeEasy.IDMEFTime_GetSec(self)
    def GetUSec(self): return _PreludeEasy.IDMEFTime_GetUSec(self)
    def GetGmtOffset(self): return _PreludeEasy.IDMEFTime_GetGmtOffset(self)
    def Clone(self): return _PreludeEasy.IDMEFTime_Clone(self)
    def ToString(self): return _PreludeEasy.IDMEFTime_ToString(self)
    def __int__(self): return _PreludeEasy.IDMEFTime___int__(self)
    def __long__(self): return _PreludeEasy.IDMEFTime___long__(self)
    def __float__(self): return _PreludeEasy.IDMEFTime___float__(self)
    def __str__(self): return _PreludeEasy.IDMEFTime___str__(self)
    def __ne__(self, *args): return _PreludeEasy.IDMEFTime___ne__(self, *args)
    def __ge__(self, *args): return _PreludeEasy.IDMEFTime___ge__(self, *args)
    def __le__(self, *args): return _PreludeEasy.IDMEFTime___le__(self, *args)
    def __eq__(self, *args): return _PreludeEasy.IDMEFTime___eq__(self, *args)
    def __gt__(self, *args): return _PreludeEasy.IDMEFTime___gt__(self, *args)
    def __lt__(self, *args): return _PreludeEasy.IDMEFTime___lt__(self, *args)
IDMEFTime_swigregister = _PreludeEasy.IDMEFTime_swigregister
IDMEFTime_swigregister(IDMEFTime)

class IDMEF(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDMEF, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDMEF, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _PreludeEasy.delete_IDMEF
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _PreludeEasy.new_IDMEF(*args)
        try: self.this.append(this)
        except: self.this = this
    def Set(self, *args): return _PreludeEasy.IDMEF_Set(self, *args)
    def Get(self, *args): return _PreludeEasy.IDMEF_Get(self, *args)
    def Clone(self, *args): return _PreludeEasy.IDMEF_Clone(self, *args)
    def ToString(self): return _PreludeEasy.IDMEF_ToString(self)
    def __str__(self): return _PreludeEasy.IDMEF___str__(self)
    def Write(self, *args): return _PreludeEasy.IDMEF_Write(self, *args)
    def Read(self, *args): return _PreludeEasy.IDMEF_Read(self, *args)
    def __rshift__(self, *args): return _PreludeEasy.IDMEF___rshift__(self, *args)
    def __lshift__(self, *args): return _PreludeEasy.IDMEF___lshift__(self, *args)
IDMEF_swigregister = _PreludeEasy.IDMEF_swigregister
IDMEF_swigregister(IDMEF)


