from app import app
from flask import request
from DistributionFactory import DistributionFactory


# PENDING, IMPELENT USING MVC?
@app.route('/getSample')
def get_sample():
    sample_size = request.args.get("sample_size")
    mean = request.args.get("mean")
    std = request.args.get("std")
    try:
        distribution = DistributionFactory.get_distribution('normal',
                                                            {'mean': float(mean), 'std': float(std)})
        sample = distribution.get_sample(int(sample_size))
        print("sample: ", sample)
    except Exception as e:
        return {'status': 'failed'}
    return {'status': 'success', 'sample': [str(e) for e in sample]}


@app.route("/getNormal")
def get_normal_sample():
    sample_size = request.args.get("sample_size")
    mean = request.args.get("mean")
    std = request.args.get("std")
    try:
        distribution = DistributionFactory.get_distribution('normal',
                                                            {'mean': float(mean), 'std': float(std)})
        sample = distribution.get_sample(int(sample_size))
        print("sample: ", sample)
    except Exception as e:
        return {'status': 'failed'}
    return {'status': 'success', 'sample': [str(e) for e in sample]}


@app.route("/getBinomial")
def get_binomial_sample():
    sample_size = request.args.get("sample_size")
    n = request.args.get("n")
    p = request.args.get("p")
    try:
        distribution = DistributionFactory.get_distribution('binomial',
                                                            {'n': float(n), 'p': float(p)})
        sample = distribution.get_sample(int(sample_size))
        print("sample: ", sample)
    except Exception as e:
        return {'status': 'failed'}
    return {'status': 'success', 'sample': [str(e) for e in sample]}


@app.route("/getNegBinomial")
def get_negbinomial_sample():
    sample_size = request.args.get("sample_size")
    r = request.args.get("r")
    p = request.args.get("p")
    try:
        distribution = DistributionFactory.get_distribution('negativebinomial',
                                                            {'r': float(r), 'p': float(p)})
        sample = distribution.get_sample(int(sample_size))
        print("sample: ", sample)
    except Exception as e:
        return {'status': 'failed'}
    return {'status': 'success', 'sample': [str(e) for e in sample]}


@app.route("/getPoisson")
def get_poisson_sample():
    sample_size = request.args.get("sample_size")
    l = request.args.get("l")
    try:
        distribution = DistributionFactory.get_distribution('poisson', {'l': float(l)})
        sample = distribution.get_sample(int(sample_size))
        print("sample: ", sample)
    except Exception as e:
        return {'status': 'failed'}
    return {'status': 'success', 'sample': [str(e) for e in sample]}


@app.route("/getExponential")
def get_exponential_sample():
    sample_size = request.args.get("sample_size")
    a = request.args.get("a")
    try:
        distribution = DistributionFactory.get_distribution('poisson', {'a': float(a)})
        sample = distribution.get_sample(int(sample_size))
        print("sample: ", sample)
    except Exception as e:
        return {'status': 'failed'}
    return {'status': 'success', 'sample': [str(e) for e in sample]}


if __name__ == "__main__":
    app.run(debug=True)
