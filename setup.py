from setuptools import setup, find_packages

setup(
    name='PromoterCalculator',
    version='1.0.0',
    author='Salis Lab',
    author_email='salis@psu.edu',
    description='A calculator for promoters',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-learn',
        'biopython',
    ],
    # additional files to include in the package
    include_package_data=True,
    package_data={
        'promoter_calculator': ['*.npy'],
    },
)