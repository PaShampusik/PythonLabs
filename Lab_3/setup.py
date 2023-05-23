from setuptools import setup


setup(
    name="Lab_3",
    version="1.0",
    description="python library for serialization",
    url="https://github.com/PaShampusik/bsuir_igi/tree/lab3/lab3",
    author="Shchirov Pavel",
    author_email="shchirovpavel@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers/json_serializer", "serializers/src",
              "serializers/xml_serializer", "serializers"],
    include_package_data=True
)
