/** Tailwind 3.4.16. Run `npm run build` after changing any part in src/parts. */
module.exports = {
  content: ['./index.html', './fa.html', './src/**/*.html'],
  theme: {
    extend: {
      colors: {
        storm: { 50:'#F1F4F4', 100:'#C3C9CA', 200:'#A5AFB1', 300:'#879497', 400:'#6A797D', 500:'#4C5F63', 600:'#2E464C', 700:'#1C3840', 800:'#153139', 900:'#0F282F', 950:'#091B20' },
        vivid: { 50:'#E6FEFE', 100:'#C0FBFB', 200:'#81F7F7', 300:'#45F3F4', 400:'#02EFF0', 500:'#02D4D5', 600:'#01A9AA', 700:'#017E7F' },
        coral: { 200:'#FFC2BA', 300:'#FF9A8F', 400:'#FF7A6B', 500:'#FF5C4D' }
      },
      fontFamily: {
        sans: ['Lexend', 'Vazirmatn', 'system-ui', 'sans-serif'],
        fa: ['Vazirmatn', 'Lexend', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace']
      }
    }
  }
};
