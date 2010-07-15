setup(
    name='Flapp',
    version='0.1',
    url='http://flapp-demo.appspot.com/',
    license='BSD',
    author='Brian Luft',
    author_email='brian@unbracketed.com',
    description='Tool for making Flask project templates ready to run on Google App Engine',
    long_description=__doc__,
    packages=['flapp'],
    namespace_packages=['flapp'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)