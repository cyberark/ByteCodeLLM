

# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ByeCodeLLM.py'],
    pathex=[],
    binaries=[('/opt/conda/lib/python3.12/site-packages/llama_cpp/lib/libllama.so', 'llama_cpp/lib'), ('/opt/conda/lib/python3.12/site-packages/llama_cpp/lib/libllava.so', 'llama_cpp/lib'), ('/opt/conda/lib/python3.12/site-packages/llama_cpp/lib/libggml-cpu.so', 'llama_cpp/lib'), ('/opt/conda/lib/python3.12/site-packages/llama_cpp/lib/libggml.so', 'llama_cpp/lib'), ('/opt/conda/lib/python3.12/site-packages/llama_cpp/lib/libggml-amx.so', 'llama_cpp/lib'), ('/opt/conda/lib/python3.12/site-packages/llama_cpp/lib/libggml-base.so', 'llama_cpp/lib')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['config.py','torch', 'transformers', 'datasets', 'nvidia-cublas-cu12', 'nvidia-cuda-runtime-cu12',
        'nvidia-cudnn-cu12', 'nvidia-cufft-cu12', 'nvidia-curand-cu12', 'nvidia-cusolver-cu12',
        'nvidia-cusparse-cu12', 'nvidia-nccl-cu12', 'nvidia-nvjitlink-cu12', 'nvidia-nvtx-cu12',
        'nvidia-cuda-cupti-cu12', 'bitsandbytes', 'xformers', 'triton'
    ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ByeCodeLLM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
