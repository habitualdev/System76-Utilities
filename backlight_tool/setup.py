from setuptools import setup


def get_requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().split('\n')


setup(
    name='s76-battery-backlight',
    version='0.1',
    description='Software to show your battery status with your keyboard backlight',
    url='#',
    author='Jean-François Labonté',
    author_email='grimsleepless@protonmail.com',
    include_package_data=True,
    install_requires=get_requirements(),
    license='Apache License 2.0',
    packages=['battery_backlight', 'battery_backlight.schema'],
    entry_points={
        'console_scripts': ['battery-backlight=battery_backlight.__main__:main']
    },
)
