from setuptools import setup


setup(
    name='cldfbench_lee_and_hasegawa2013',
    py_modules=['cldfbench_lee_and_hasegawa2013'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'lee_and_hasegawa2013=cldfbench_lee_and_hasegawa2013:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
