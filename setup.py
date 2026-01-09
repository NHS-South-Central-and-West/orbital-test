from setuptools import setup, find_packages

setup(
    name='orbital-test',
    version='0.1.0',
    description='Demonstration of Posit\'s Orbital Package',
    author='Specialist Analytics Team - BI Analytics - South, Central and West CSU',
    author_email='scwcsu.analytics.specialist@nhs.net',
    package_dir={"": "src"},
    packages=find_packages(where="src"),    
    install_requires=[
        'ipykernel',
        'orbital',  # comes with scikit-learn
        'pandas',
        'pyodbc',
        'sqlalchemy'
    ],
)