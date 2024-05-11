import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      backgroundColor: {
        'udemyPurple': 'rgba(86, 36, 208, 1)',
      },
      textColor: {
        'udemyPurple': 'rgba(86, 36, 208, 1)',
      },
      stroke: {
        'udemyPurple': 'rgba(86, 36, 208, 1)',
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      "acid",
      // "winter"
    ],
  },
};
export default config;
