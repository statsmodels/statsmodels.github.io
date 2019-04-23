# Statsmodels Documentation Website

Hosted at [www.statsmodels.org](https://www.statsmodels.org).

## Updating

- Build the docs with sphinx
- Copy the HTML output to a directory with the version name e.g. (`0.8.0`)
- Update the symlinks
  + For the stable version, change `stable`: `ln -s 0.8.0 stable`
  + For the development version, change `devel`: `ln -s 0.8.1 devel`
  + The `dev` symlink points to `devel`
