from setuptools import setup, find_packages

long_description = 'Package to analyse cryo-EM reconstruction'

setup(
		name ='qcheck',
		version ='1.0.0',
		author ='kutumbarao Nidamarthi',
		author_email ='nidamarthi.kr@gmail.com',
		url ='https://github.com/nidamarthikr/qcheck',
		description ='Quality parameters for cryoEM',
		license ='MIT',
		packages = find_packages(),
		classifiers =[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		],
	      	keywords ='CryoEm 3D maps Reconstrunction Statistics Quality matrics',
		install_requires = ['python >=3', 
                                     'pandas >=1.3.5',
                                     'mrcfile >=1.4.3',
                                     'h5py >=3.9.0'],
		zip_safe = False
)

