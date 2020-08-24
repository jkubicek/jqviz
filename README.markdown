# Deploying

I stole these deployment instructions from [hynek.me](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)

```bash
python -m pep517.build .
twine upload -r test --sign dist/jqviz-0.0.1*
```