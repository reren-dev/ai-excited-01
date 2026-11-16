import { copyFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync('entry.png', join(outDir, 'entry.png'));
console.log(`Successfully copied entry.png to ${outDir}/entry.png`);
