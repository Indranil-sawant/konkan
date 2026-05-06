/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./*/templates/**/*.html",
    "./**/templates/**/*.html",
    "./static/js/**/*.js",
  ],
  corePlugins: {
    preflight: false,
  },
  theme: {
    extend: {
      colors: {
        ocean: {
          deep: "#0a3d62",
          mid: "#0077b6",
          light: "#48cae4",
        },
        aqua: {
          mist: "#caf0f8",
        },
        sand: {
          warm: "#fdf0d5",
        },
        sunset: {
          coral: "#ff7b54",
          gold: "#ffb703",
        },
        foam: "#f8fafc",
        navy: {
          dark: "#1b263b",
        },
      },
      fontFamily: {
        sans: ["Manrope", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["Playfair Display", "ui-serif", "Georgia", "serif"],
      },
      boxShadow: {
        coastal: "0 12px 30px rgba(0, 119, 182, 0.15)",
        "coastal-sm": "0 4px 12px rgba(0, 119, 182, 0.08)",
      },
      borderRadius: {
        coastal: "16px",
      },
    },
  },
  plugins: [],
};
