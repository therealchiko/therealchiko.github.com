import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';

const require = createRequire(import.meta.url);
const fonts = [400, 800].map(weight => ({
  name: 'Archivo',
  data: readFileSync(require.resolve(`@fontsource/archivo/files/archivo-latin-${weight}-normal.woff`)),
  weight,
  style: 'normal',
}));

// Fonts ship with the build: local and CI renders never depend on system fonts.
export async function renderSocialImage(title, article = false) {
  for (let fontSize = 102; fontSize >= 36; fontSize -= 2) {
    let titleBounds;
    const text = (children, style, extra = {}) => ({ type: 'div', props: { children, style, ...extra } });
    const svg = await satori(text([
      ...(!article ? [text('Chiko Mukwenha', { position: 'absolute', left: 82, top: 64, fontSize: 30, fontWeight: 800 })] : []),
      text(title, {
        position: 'absolute', left: 82, top: 160, width: 1036,
        fontSize, fontWeight: 800, lineHeight: 1.08, letterSpacing: -3,
        overflowWrap: 'break-word',
      }, { id: 'card-title' }),
      ...(!article ? [text('Software, products and figuring things out.', {
        position: 'absolute', left: 82, top: 394, fontSize: 30,
      })] : []),
      text('chikomukwenha.co', { position: 'absolute', left: 82, bottom: 56, fontSize: 25 }),
      ...(article ? [text('An essay by Chiko', { position: 'absolute', right: 82, bottom: 56, fontSize: 25 })] : []),
    ], {
      width: 1200, height: 630, position: 'relative', display: 'flex',
      backgroundColor: '#edea32', color: '#20382d', fontFamily: 'Archivo', fontWeight: 400,
    }), {
      width: 1200, height: 630, fonts,
      onNodeDetected(node) { if (node.props.id === 'card-title') titleBounds = node; },
    });
    // Measure the actual font layout, including long words, before accepting it.
    if (titleBounds && titleBounds.height <= (article ? 330 : 210) && titleBounds.width <= 1036) {
      return new Resvg(svg).render().asPng();
    }
  }
  throw new Error(`Social card title is too long to fit: ${title}`);
}
