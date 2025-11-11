from setuptools import find_packages, setup

package_name = 'auv_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juicy',
    maintainer_email='juicy@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'webcam = auv_vision.camera_node:main',
        'operations = auv_vision.operations_node:main',
        'pixel_width_subscriber = auv_vision.pixel_width_subscriber:main',
        'distance = auv_vision.distance_node:main',
        ],
    },
)
