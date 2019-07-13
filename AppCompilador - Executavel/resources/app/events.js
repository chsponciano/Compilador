const fs = require("fs");
const {
    dialog
} = require("electron").remote;
const {
    clipboard
} = require("electron").remote;
const child = require('child_process').execFile;
const path = require("path");
const options = {
    filters: [{
        name: 'Text',
        extensions: ['txt']
    }]
};
var ehNovo = true;
var keypressold;

autoResize();

function novo() {
    console.log("Iniciada Função novo");
    document.getElementById('area-codigo-fonte').value = "";
    document.getElementById('area-mensagem').value = "";
    document.getElementById('area-status').innerHTML = "";
    ehNovo = true;
    console.log("Finalizada Função novo");
}

function abrir() {
    console.log("Iniciada Função abrir");

    dialog.showOpenDialog(null, options, (filename) => {
        if (filename == undefined) {
            return;
        }

        fs.readFile(filename[0], {
            encoding: 'latin1'
        }, (err, data) => {
            if (err) {
                alert("Erro ao ler o arquivo");
                return;
            }

            document.getElementById('area-codigo-fonte').value = data;
            document.getElementById('area-mensagem').value = "";
            document.getElementById('area-status').innerHTML = String(filename);
            ehNovo = false;
        });


    });

    console.log("Finalizada Função abrir");
}

function getExtensao(path) {
    var final = path.substr(path.lastIndexOf('/') + 1);
    var separador = final.lastIndexOf('.');
    return separador <= 0 ? '' : final.substr(separador + 1);
}

function salvar() {
    console.log("Iniciada Função salvar");

    let content = document.getElementById('area-codigo-fonte').value;

    if (ehNovo) {
        dialog.showSaveDialog(null, options, (filename) => {
            if (filename == undefined)
                return

            if (getExtensao("/" + filename) != "TXT") {
                var pos = filename.lastIndexOf('.');

                if (pos > 0) {
                    filename = filename.substr(0, pos);
                }

                filename += ".txt";
            }

            fs.writeFile(filename, content, (err) => {
                if (err) {
                    alert("Erro ao salvar arquivo");
                    return;
                }
                alert("Arquivo Salvo com Sucesso");
                ehNovo = false;
                document.getElementById('area-mensagem').value = "";
                document.getElementById('area-status').innerHTML = String(filename);
            });

        });
    } else {
        var filename = document.getElementById('area-status').innerHTML;
        fs.writeFile(filename, content, (err) => {
            if (err) {
                alert("Erro ao salvar arquivo");
                return;
            }
            alert("Arquivo Salvo com Sucesso");
            ehNovo = false;
            document.getElementById('area-mensagem').value = "";
            document.getElementById('area-status').innerHTML = String(filename);
        });
    }
    console.log("Finalizada Função salvar");
}

function copiar() {
    console.log("Iniciada Função Copiar");
    let copy = '';

    if (window.getSelection) {
        copy = String(window.getSelection());
    } else if (document.selection) {
        copy = document.selection.createRange().text;
    }

    clipboard.writeText(copy);
    console.log("Finalizada Função Copiar");
}

function colar() {
    console.log("Iniciada Função Colar");
    var selector = document.querySelector("textarea");
    selector.value = selector.value.substring(0, selector.selectionStart) + clipboard.readText() + selector.value.substring(selector.selectionEnd);
    console.log("Finalizada Função Colar");
}

function recortar() {
    console.log("Iniciada Função Recortar");
    copiar();
    var selector = document.querySelector("textarea");
    selector.value = selector.value.substring(0, selector.selectionStart) + '' + selector.value.substring(selector.selectionEnd);
    console.log("Finalizada Função Recortar");
}

function preCompilacao() {
    var code = document.getElementById('area-codigo-fonte').value;

    if (code.length == 0) {
        document.getElementById('area-mensagem').value = "Nenhum programa para compilar!";
    } else {
        var dir = document.getElementById('area-status').innerHTML;
        let content = document.getElementById('area-codigo-fonte').value;

        if (dir.length == 0) {
            dialog.showSaveDialog(null, options, (filename) => {
                if (filename == undefined)
                    return

                if (getExtensao("/" + filename) != "TXT") {
                    var pos = filename.lastIndexOf('.');

                    if (pos > 0) {
                        filename = filename.substr(0, pos);
                    }

                    filename += ".txt";
                }

                fs.writeFile(filename, content, (err) => {
                    if (err) {
                        alert("Erro ao salvar arquivo");
                        return;
                    }
                    ehNovo = false;
                    document.getElementById('area-mensagem').value = "";
                    document.getElementById('area-status').innerHTML = String(filename);

                    compilar(code, filename);
                });
            });
        } else {
            compilar(code, dir);
        }
    }

    function compilar(code, dir) {
        let action = path.join(__dirname, '/script/dist/Main/Main.exe');

        child(action, [code, dir], function(err, results) {
            if (err) alert(err);

            var out = "";
            if (results.length == 0) {
                out = "Programa compilado com sucesso";
            } else {
                for (var i = 0; i < results.length; i++) {
                    out += results[i];
                }
            }

            document.getElementById('area-mensagem').value = out;
        });
    }
}

async function executar() {
    var path = updateExtension(document.getElementById('area-status').innerHTML, '.il');
    const exec = require('child_process').exec;

    try {
        if (path.length > 0 && fs.existsSync(path)) {

            var command = 'C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\ilasm.exe ' + path;
            await exec(command, (err, stdout, stderr) => {
                if (stderr) {
                    document.getElementById('area-mensagem').value = stderr;
                    return;
                }
                document.getElementById('area-mensagem').value = stdout;
            });

            command = 'start cmd /k' + updateExtension(path, '.exe');
            await exec(command, (err, stdout, stderr) => {
                if (stderr) {
                    document.getElementById('area-mensagem').value = stderr;
                    return;
                }
                document.getElementById('area-mensagem').value = stdout;
            });

        } else {
            document.getElementById('area-mensagem').value = 'Nenhum programa aberto ou compilado para ser executado!';
        }
    } catch (err) {
        document.getElementById('area-mensagem').value = err;
    }

    function updateExtension(path, extension) {
        var pos = path.lastIndexOf('.');

        if (pos > 0) {
            path = path.substr(0, pos);
        }
        path += extension;
        return path;
    }
}

function equipe() {
    document.getElementById('area-mensagem').value = "=========================== Desenvolvimento ==========================\nAcademicos: Carlos Henrique Ponciano da Silva & Vinicius Luis da Silva";
}

function autoResize() {
    console.log("AutoResize");
    var resto = parseInt(window.innerHeight) - 230;
    document.getElementById("area-codigo-fonte").style.minHeight = String(resto) + 'px';
}

window.addEventListener('resize', function() {
    autoResize();
});

document.getElementById('area-codigo-fonte').addEventListener('keydown', function(e) {
    if (e.keyCode === 9) {
        e.target.value = e.target.value.substring(0, this.selectionStart) +
            '\t' +
            e.target.value.substring(this.selectionEnd);
        this.selectionStart = this.selectionStart + 1;
        this.selectionEnd = this.selectionStart + 1;
        e.preventDefault();
    }
}, false);

window.addEventListener("keydown", function(event) {
    //ctrl+n - 17+78
    if (keypressold == 17 && event.keyCode == 78) {
        novo();
    }

    //ctrl+o - 17+79
    if (keypressold == 17 && event.keyCode == 79) {
        abrir();
    }

    //ctrl+s - 17+83
    if (keypressold == 17 && event.keyCode == 83) {
        salvar();
    }

    //ctrl+c - 17+67
    if (keypressold == 17 && event.keyCode == 67) {
        copiar();
    }

    //ctrl+v - 17+86
    if (keypressold == 17 && event.keyCode == 86) {
        colar();
    }

    //ctrl+x - 17+88
    if (keypressold == 17 && event.keyCode == 88) {
        recortar();
    }

    //F9 - 120
    if (event.keyCode == 120) {
        compilar();
    }

    //F1 - 112
    if (event.keyCode == 112) {
        equipe();
    }

    // ctrl+e 17+69
    if (keypressold == 17 && event.keyCode == 69) {
        executar();
    }

    keypressold = event.keyCode;
});