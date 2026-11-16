import * as fs from 'fs';
import * as path from 'path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
fs.mkdirSync(outDir, { recursive: true });
fs.copyFileSync('entry.png', path.join(outDir, 'entry.png'));
console.log(`Copied entry.png to ${path.join(outDir, 'entry.png')}`);
