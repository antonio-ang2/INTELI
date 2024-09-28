const express = require('express');
const multer = require('multer');
const os = require('os');
const path = require('path');
const fs = require('fs');

// Configuração do servidor
const app = express();
const port = 8000;

// Configuração do multer para armazenar as imagens recebidas
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    // Define o diretório onde as imagens serão salvas
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    // Define o nome do arquivo com o timestamp atual
    cb(null, 'image_' + Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });

// Função para obter o IP local da máquina
function getLocalIP() {
  const interfaces = os.networkInterfaces();
  for (let iface in interfaces) {
    for (let alias of interfaces[iface]) {
      if (alias.family === 'IPv4' && !alias.internal) {
        return alias.address;
      }
    }
  }
  return 'localhost';
}

// Rota POST para receber a imagem
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('Nenhuma imagem foi enviada');
  }

  // A imagem foi salva com sucesso
  console.log(`Imagem recebida e salva como: ${req.file.filename}`);
  res.status(200).send('Upload concluído com sucesso!');
});

// Cria a pasta 'uploads' se ela não existir
if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads');
}

// Inicia o servidor e exibe a URL completa
app.listen(port, () => {
  const localIP = getLocalIP();
  const serverUrl = `http://${localIP}:${port}`;
  console.log(`Servidor rodando na URL: ${serverUrl}`);
});
