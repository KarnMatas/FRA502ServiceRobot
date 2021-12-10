import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
package_name = 'dd_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name), glob('Launch/*.py')),
        # Include model and simulation files
        (os.path.join('share', package_name), glob('Models/*.urdf')),
        (os.path.join('share', package_name), glob('Worlds/*.world')),
        (os.path.join('share', package_name), glob('rviz/*')),
        (os.path.join('share', package_name), glob('param/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='ROS 2 Developer',
    author_email='ros2@ros.com',
    maintainer='karn',
    maintainer_email='ma.ta.s.karn@gmail.com',
    
    keywords=['foo', 'bar'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Apache License 2.0',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    
    description='dd_robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'jointstate_pub = dd_robot.mc_jointstate_pub:main',
            'nav_pub = dd_robot.navgoal:main'
        ],
    },
)
