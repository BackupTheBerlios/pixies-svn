
dist:
	make -C docs/
	./setup.py sdist --formats=zip,gztar,bztar
	./setup.py bdist_rpm

clean:
	rm -rf build/ dist/ MANIFEST
	find -name '*.pyc *~' | xargs rm -f
