from setuptools import setup, find_packages
#from src.qcheck.pc_sk import pc_sk

setup(
		name ='cryoPack',
		version ='0.0.1',
		author ='kutumbarao Nidamarthi',
		author_email ='nidamarthi.kr@gmail.com',
		url ='https://github.com/nidamarthikr/cryoPack',
		description ='Quality parameters for cryoEM',
		license ='MIT',
		packages = find_packages(),
		classifiers =[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		],
	      	keywords ='CryoEm 3D maps Reconstrunction Statistics Quality matrics',
		install_requires = [
                                     'pandas',
                                     'mrcfile',
                                     'h5py', 
			             'scikit-image'],
	        entry_points={
			 'console_scripts': ["cP.qcheck_pc=src.qcheck.pc_sk:main"],
		},
	        long_description=open('README.md').read(),
                long_description_content_type='text/markdown',
		zip_safe = False
)

