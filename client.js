const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const readline = require('readline');

const protoPath = 'p2pfileshare.proto';
const packageDefinition = protoLoader.loadSync(protoPath, {});
const p2pFileShare = grpc.loadPackageDefinition(packageDefinition).p2pfileshare;

const client = new p2pFileShare.FileShareService('localhost:50051', grpc.credentials.createInsecure());

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function listFiles() {
  client.ListFiles({}, (error, response) => {
    if (!error) {
      console.log('Archivos disponibles:', response.filenames.join(', '));
    } else {
      console.error('Error al listar archivos:', error.message);
    }
    askForAction();
  });
}

function downloadFile() {
  // Implementación ficticia de descarga
  console.log("Archivo 'dummy.txt' descargado exitosamente.");
  askForAction();
}

function uploadFile() {
  // Implementación ficticia de carga
  console.log("Archivo 'dummy.txt' cargado exitosamente.");
  askForAction();
}

function askForAction() {
  rl.question('Seleccione una acción (1: Listar archivos, 2: Descargar archivo, 3: Cargar archivo, 4: Salir): ', (answer) => {
    switch(answer) {
      case '1':
        listFiles();
        break;
      case '2':
        downloadFile();
        break;
      case '3':
        uploadFile();
        break;
      case '4':
        rl.close();
        break;
      default:
        console.log('Opción no reconocida.');
        askForAction();
    }
  });
}

askForAction();
