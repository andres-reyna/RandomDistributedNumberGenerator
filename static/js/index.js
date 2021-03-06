function getUrl(distribution, sample_size) {
    url = ''
    if(distribution == 'normal') {
        mean = document.getElementById('n-mean').value
        std = document.getElementById('n-std').value

        url = '/getNormal?mean=' + mean + "&std=" + std + "&sample_size=" + sample_size
    }
    else if(distribution == 'binomial') {
        n = document.getElementById('b-n').value
        p = document.getElementById('b-p').value

        url = '/getBinomial?n=' + n + "&p=" + p + "&sample_size=" + sample_size
    }
    else if(distribution == 'negbinomial') {
        r = document.getElementById('nb-r').value
        p = document.getElementById('nb-p').value

        url = '/getNegBinomial?r=' + r + "&p=" + p + "&sample_size=" + sample_size
    }
    else if(distribution == 'poisson') {
        l = document.getElementById('p-l').value

        url = '/getPoisson?l=' + l + "&sample_size=" + sample_size
    }
    else if(distribution == 'exponential') {
        a = document.getElementById('e-a').value

        url = '/getExponential?a=' + a + "&sample_size=" + sample_size
    }
    return url
}

xhr = new XMLHttpRequest()
document.getElementById('btn-get-sample').onclick = (e) => {
    distribution = document.getElementById('select-distribution').value

    sample_size = document.getElementById('sample-size').value

    url = getUrl(distribution, sample_size)
    xhr.open( "GET", url, false); // false for synchronous request
    xhr.send(null);

    response = JSON.parse(xhr.responseText)

    if(response.status == 'success') {
       content = response.sample.join(' , ')
       document.getElementById("result").innerHTML = content
    }
    else {
        console.log(response.error)
    }
}

function hideAllInputs() {
    document.getElementById('normal').style.display = "none"
    document.getElementById('binomial').style.display = "none"
    document.getElementById('negbinomial').style.display = "none"
    document.getElementById('poisson').style.display = "none"
    document.getElementById('exponential').style.display = "none"
}

function clearInputs(){
    document.getElementById('result').innerHTML = '';
    document.getElementById('n-mean').value = '';
    document.getElementById('n-std').value = '';
    
    document.getElementById('b-n').value = '';
    document.getElementById('b-p').value = '';

    document.getElementById('p-l').value = '';

    document.getElementById('e-a').value = '';

    document.getElementById('sample-size').value = '';
}

document.getElementById('select-distribution').onchange = (e) => {
    distribution = document.getElementById('select-distribution').value
    hideAllInputs()
    clearInputs()
    document.getElementById(distribution).style.display = "block"
}