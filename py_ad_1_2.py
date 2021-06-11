"""
Section 1
Multithreading - Python's Gil
Keyword - CPython, 메모리 관리, GIL 사용 이유
"""
"""
GIL(Global Interpreter Lock)
    (1). CPython -> Python (bytecode) 실행 시 여러 thread 사용할 경우
        단일 스레드만이 Python object에 접근하게 제한하는 mutex
    (2). CPython 메모리 관리가 취약하기 때문 (즉, Thread-safe)
    (3). 단일 스레드로 충분히 빠르다.
    (4). 프로세스 사용 가능 (Numpy/Scipy) 등 GIL 외부 영역에서 효율적인 코딩이 가능한 library들이 존재함.
    (5). 병렬 처리는 Multiprocessing, asyncio 등 선택지가 다양함.
    (6). thread 동시성 완벽 처리를 위해 -> Jython, IronPython, Stackless Python 등이 존재함.
"""