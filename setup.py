import setuptools

setuptools.setup(
    name="autodrag",
    packages = ['autodrag'],
    version="0.1.0",
    license = "MIT",
    description="Resizing matplotlib subplots to fit a canvas",
    author="Suraj Gowda",
    url="https://github.com/sgowda/jupyter-subplot-layout-widget/tree/master/python",
    download_url='https://sgowda/jupyter-subplot-layout-widget/archive/v_0.1.0.tar.gz',
    keywords=['matplotlib', 'figure layout', 'tools'],
    install_requires=['matplotlib', 'numpy'],
    classifiers = [
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
