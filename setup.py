from setuptools import setup, find_packages

long_description = 'Countdown timer!'

setup(
  name = 'pycountdown',
  version = '2.0',
  license='Apache',
  description = 'Countdown timer!',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/badsql-tools',
  download_url = 'https://github.com/nayakrujul/countdowntimer/archive/refs/tags/v_01.tar.gz',
  keywords = ['countdown', 'timer'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points ={
            'console_scripts': [
                'countdowndemo = countdowntimer.countdown_program:countdown',
                'countdown = countdowntimer.countdown_program:countdown_terminal'
            ]
  }
)
