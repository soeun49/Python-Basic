from .database import *
#   현재 디렉터리 안에 있는 database 모듈로부터 모든것을 import
#__init__.py
#   패키지 import할 때 초기화 작업을 수행하는 파일
#   기본적으로는 없어도 패키지로 인식

# from 패키지 import*: 내부에 있는 모든 객체를 import

__all__ = ["Database"] #명시된 심볼만 export!
# __all__=[] #*로 임포트시 아무것도 export 하지 않음

