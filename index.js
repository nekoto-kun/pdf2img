import fs from 'fs';
import pdf2img from 'pdf-img-convert';

const config = {
  outputFormat: 'png',
  outputType: 'file',
  pageNumbers: 'all',
};

(async function () {
  // Find current directory for PDF files
  const files = fs.readdirSync('./')
  const pdfFiles = files.filter(file => file.endsWith('.pdf'))

  // Check if PDF files exist
  if (pdfFiles.length === 0) {
    console.log('No PDF files found!')
    return
  }

  // Check if output directory exists
  if (!fs.existsSync('output')) {
    fs.mkdirSync('output')
  }

  // Clear output directory
  fs.readdirSync('./output').forEach(file => {
    fs.unlinkSync(`./output/${file}`)
  })

  // Convert PDF to images
  pdfFiles.forEach(async file => {
    console.log(`Converting ${file} to images...`)
    const pdfArray = await pdf2img.convert(`./${file}`, {
      ...config,
      outputName: `${file}`,

    })

    // Write images to output directory
    for (let i = 0; i < pdfArray.length; i++) {
      fs.writeFileSync(`./output/${file.replace('.pdf', '')}-${i}.png`, pdfArray[i], 'binary', err => {
        if (err) {
          console.log(err)
        }
      })
    }

    console.log('Done!')
  })
})();