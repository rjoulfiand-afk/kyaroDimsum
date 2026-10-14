const MENU_ITEMS = [
  // --- DIMSUM MENTAI (Warna Kuning & Logo K) ---
  {
    id: "dm-3",
    name: "Dimsum Mentai Isi 3",
    category: "dimsum-mentai",
    type: "makanan",
    price: 13000,
    desc: "3 pcs dimsum ayam lembut diselimuti saus mentai gurih torched khas Kyaro.",
    image: "assets/mentai_crop.png",
    theme: "theme-mentai",
    badge: { text: "KYARO K", type: "mentai-k" },
    available: true
  },
  {
    id: "dm-6",
    name: "Dimsum Mentai Isi 6",
    category: "dimsum-mentai",
    type: "makanan",
    price: 21000,
    desc: "6 pcs dimsum ayam lembut porsi favorit dengan limpahan saus mentai torched.",
    image: "assets/mentai_crop.png",
    theme: "theme-mentai",
    badge: { text: "KYARO K", type: "mentai-k" },
    available: true
  },
  {
    id: "dm-8",
    name: "Dimsum Mentai Isi 8",
    category: "dimsum-mentai",
    type: "makanan",
    price: 29000,
    desc: "8 pcs dimsum ayam lezat dengan saus mentai gurih dan taburan parsley.",
    image: "assets/mentai_crop.png",
    theme: "theme-mentai",
    badge: { text: "KYARO K", type: "mentai-k" },
    available: true
  },
  {
    id: "dm-10",
    name: "Dimsum Mentai Isi 10",
    category: "dimsum-mentai",
    type: "makanan",
    price: 36000,
    desc: "10 pcs dimsum ayam mantap untuk dinikmati berdua, creamy & smoky.",
    image: "assets/mentai_crop.png",
    theme: "theme-mentai",
    badge: { text: "KYARO K", type: "mentai-k" },
    available: true
  },
  {
    id: "dm-16",
    name: "Dimsum Mentai Isi 16",
    category: "dimsum-mentai",
    type: "makanan",
    price: 56000,
    desc: "16 pcs dimsum mentai porsi kumpul keluarga / nongkrong seru.",
    image: "assets/mentai_crop.png",
    theme: "theme-mentai",
    badge: { text: "KYARO K", type: "mentai-k" },
    available: true
  },
  {
    id: "dm-20",
    name: "Dimsum Mentai Isi 20",
    category: "dimsum-mentai",
    type: "makanan",
    price: 68000,
    desc: "20 pcs dimsum mentai platter komplit jumbo paling hemat & puas.",
    image: "assets/mentai_crop.png",
    theme: "theme-mentai",
    badge: { text: "KYARO K", type: "mentai-k" },
    available: true
  },

  // --- DIMSUM HOT LAVA (Warna Merah) ---
  {
    id: "dhl-3",
    name: "Dimsum Hot Lava Isi 3",
    category: "dimsum-hot-lava",
    type: "makanan",
    price: 13000,
    desc: "3 pcs dimsum pedas nampol bermandikan saus hot lava cabai pilihan.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-hotlava",
    badge: { text: "HOT LAVA 🌶️", type: "hotlava-fire" },
    available: true
  },
  {
    id: "dhl-6",
    name: "Dimsum Hot Lava Isi 6",
    category: "dimsum-hot-lava",
    type: "makanan",
    price: 21000,
    desc: "6 pcs dimsum pedas gurih nagih dengan aroma cabe segar khas Kyaro.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-hotlava",
    badge: { text: "HOT LAVA 🌶️", type: "hotlava-fire" },
    available: true
  },
  {
    id: "dhl-8",
    name: "Dimsum Hot Lava Isi 8",
    category: "dimsum-hot-lava",
    type: "makanan",
    price: 29000,
    desc: "8 pcs dimsum berbalut saus lava pedas membara bikin melek.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-hotlava",
    badge: { text: "HOT LAVA 🌶️", type: "hotlava-fire" },
    available: true
  },
  {
    id: "dhl-10",
    name: "Dimsum Hot Lava Isi 10",
    category: "dimsum-hot-lava",
    type: "makanan",
    price: 36000,
    desc: "10 pcs dimsum saus hot lava pedas mantap untuk pecinta cita rasa pedas.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-hotlava",
    badge: { text: "HOT LAVA 🌶️", type: "hotlava-fire" },
    available: true
  },
  {
    id: "dhl-16",
    name: "Dimsum Hot Lava Isi 16",
    category: "dimsum-hot-lava",
    type: "makanan",
    price: 56000,
    desc: "16 pcs party portion dimsum hot lava cocok untuk makan ramean.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-hotlava",
    badge: { text: "HOT LAVA 🌶️", type: "hotlava-fire" },
    available: true
  },
  {
    id: "dhl-20",
    name: "Dimsum Hot Lava Isi 20",
    category: "dimsum-hot-lava",
    type: "makanan",
    price: 68000,
    desc: "20 pcs porsi jumbo dimsum hot lava spesial Kyaro sensasi pedas pol.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-hotlava",
    badge: { text: "HOT LAVA 🌶️", type: "hotlava-fire" },
    available: true
  },

  // --- ADDITIONAL / EKSTRA ---
  {
    id: "add-steam",
    name: "Dimsum Steam",
    category: "additional",
    type: "makanan",
    price: 3500,
    desc: "Dimsum ayam kukus original per pcs, tekstur kenyal dan juicy.",
    image: "assets/hot_lava_crop.png",
    theme: "theme-additional",
    badge: { text: "STEAM", type: "generic" },
    available: true
  },
  {
    id: "add-chili",
    name: "Chili Oil",
    category: "additional",
    type: "makanan",
    price: 2500,
    desc: "Minyak cabai racikan khas Kyaro gurih dan beraroma harum rempah.",
    image: "assets/chili_oil.png",
    theme: "theme-additional",
    badge: { text: "CHILI OIL", type: "generic" },
    available: true
  },
  {
    id: "add-moza",
    name: "Mozarella (Ekstra)",
    category: "additional",
    type: "makanan",
    price: 2000,
    desc: "Topping keju mozarella leleh mulur yang gurih di atas dimsum hangat.",
    image: "assets/mozarella.png",
    theme: "theme-additional",
    badge: { text: "MOZARELLA", type: "generic" },
    available: true
  },
  {
    id: "add-saos",
    name: "Saos Sachet",
    category: "additional",
    type: "makanan",
    price: 500,
    desc: "Ekstra saus sachet pelengkap dimsum.",
    image: "assets/logo_kyaro.png",
    theme: "theme-additional",
    badge: { text: "SAOS", type: "generic" },
    available: true
  },

  // --- COFFEE SERIES ---
  {
    id: "cof-aren",
    name: "Kopi Susu Gula Aren",
    category: "coffee",
    type: "minuman",
    price: 10000,
    desc: "Espresso mantap berpadu susu segar dan manis legit gula aren murni.",
    image: "assets/coffee_cup.png",
    theme: "theme-coffee",
    badge: { text: "BEST COFFEE", type: "generic" },
    available: true
  },
  {
    id: "cof-nusantara",
    name: "Kopi Susu Nusantara",
    category: "coffee",
    type: "minuman",
    price: 10000,
    desc: "Kopi susu tradisional citarasa khas rempah Nusantara creamy.",
    image: "assets/coffee_cup.png",
    theme: "theme-coffee",
    badge: { text: "COFFEE", type: "generic" },
    available: true
  },
  {
    id: "cof-americano",
    name: "Americano Coffee",
    category: "coffee",
    type: "minuman",
    price: 10000,
    desc: "Kopi hitam klasik dari biji pilihan tanpa gula, segar & berenergi.",
    image: "assets/coffee_cup.png",
    theme: "theme-coffee",
    badge: { text: "COFFEE", type: "generic" },
    available: true
  },
  {
    id: "cof-cappucino",
    name: "Cappucino Coffee",
    category: "coffee",
    type: "minuman",
    price: 10000,
    desc: "Perpaduan espresso kental dengan foam susu lembut yang menenangkan.",
    image: "assets/coffee_cup.png",
    theme: "theme-coffee",
    badge: { text: "COFFEE", type: "generic" },
    available: true
  },
  {
    id: "cof-matchapresso",
    name: "Matchapresso",
    category: "coffee",
    type: "minuman",
    price: 10000,
    desc: "Fusion unik espresso kopi pekat berlayer matcha premium Kyaro.",
    image: "assets/drinks_crop.png",
    theme: "theme-coffee",
    badge: { text: "SPECIAL FUSION", type: "generic" },
    available: true
  },

  // --- MATCHA SERIES ---
  {
    id: "mat-sig",
    name: "Signature Matcha",
    category: "matcha",
    type: "minuman",
    price: 13000,
    desc: "Matcha Jepang otentik kental, wangi khas dan lembut creamy di lidah.",
    image: "assets/matcha_cup.png",
    theme: "theme-matcha",
    badge: { text: "SIGNATURE", type: "generic" },
    available: true
  },
  {
    id: "mat-latte",
    name: "Choco Matcha Latte",
    category: "matcha",
    type: "minuman",
    price: 15000,
    desc: "Kombinasi mewah bubuk cokelat premium, matcha pekat & susu segar.",
    image: "assets/drinks_crop.png",
    theme: "theme-matcha",
    badge: { text: "PREMIUM", type: "generic" },
    available: true
  },
  {
    id: "mat-cano",
    name: "Matcharicano",
    category: "matcha",
    type: "minuman",
    price: 13000,
    desc: "Matcha segar ringan sensasi americano dingin pelepas dahaga.",
    image: "assets/matcha_cup.png",
    theme: "theme-matcha",
    badge: { text: "MATCHA", type: "generic" },
    available: true
  },
  {
    id: "mat-berry",
    name: "Matchaberry",
    category: "matcha",
    type: "minuman",
    price: 13000,
    desc: "Kombinasi matcha autentik dengan manis asam sari buah berry segar.",
    image: "assets/matcha_cup.png",
    theme: "theme-matcha",
    badge: { text: "MATCHA", type: "generic" },
    available: true
  },

  // --- CHOCOLATE SERIES ---
  {
    id: "cho-sig",
    name: "Signature Chocolate",
    category: "chocolate",
    type: "minuman",
    price: 10000,
    desc: "Cokelat pekat pilihan kaya rasa manis pas disajikan dingin segar.",
    image: "assets/choco_cup.png",
    theme: "theme-choco",
    badge: { text: "SIGNATURE", type: "generic" },
    available: true
  },
  {
    id: "cho-coffee",
    name: "Choco Coffee",
    category: "chocolate",
    type: "minuman",
    price: 13000,
    desc: "Perpaduan seimbang rasa cokelat mantap dan kopi harum menggugah selera.",
    image: "assets/choco_cup.png",
    theme: "theme-choco",
    badge: { text: "CHOCOLATE", type: "generic" },
    available: true
  }
];

// ==========================================
// 2. STATE MANAGEMENT & STORAGE KEYS
// ==========================================
const STORAGE_KEYS = {
  TRANSACTIONS: "kyaro_pos_transactions_v2",
  ADMIN_NOTES: "kyaro_pos_admin_notes_v2",
  MENU_STOCK: "kyaro_pos_menu_stock_v2",
  SOUND_ENABLED: "kyaro_pos_sound_pref"
};

// Current Session State
let state = {
  currentTab: "pos",
  activeCategory: "all",
  searchKeyword: "",
  cart: [],
  orderType: "Dine In",
  customerName: "Pelanggan",
  tableNumber: "01",
  generalOrderNote: "",
  discount: { type: "fixed", value: 0 },
  currentOrderNumber: 1,
  currentPaymentMethod: "Tunai",
  cashPaidAmount: 0,
  activeItemNoteId: null,
  soundEnabled: true,
  reportFilter: {
    period: "today",
    customDate: null,
    paymentMethod: "all",
    search: ""
  }
};

// ==========================================
// 3. SOUND SYNTHESIZER (WEB AUDIO API)
// ==========================================
class SoundFX {
  constructor() {
    this.ctx = null;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.ctx = new AudioContext();
      }
    }
  }

  playBeep() {
    if (!state.soundEnabled) return;
    try {
      this.init();
      if (!this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(650, this.ctx.currentTime);
      gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.1);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.1);
    } catch (e) {
      console.warn("Audio play error", e);
    }
  }

  playCashRegister() {
    if (!state.soundEnabled) return;
    try {
      this.init();
      if (!this.ctx) return;
      const now = this.ctx.currentTime;

      // Bell chime 1
      const osc1 = this.ctx.createOscillator();
      const gain1 = this.ctx.createGain();
      osc1.type = "triangle";
      osc1.frequency.setValueAtTime(987.77, now); // B5
      gain1.gain.setValueAtTime(0.2, now);
      gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
      osc1.connect(gain1);
      gain1.connect(this.ctx.destination);
      osc1.start(now);
      osc1.stop(now + 0.4);

      // Bell chime 2 (higher note)
      const osc2 = this.ctx.createOscillator();
      const gain2 = this.ctx.createGain();
      osc2.type = "sine";
      osc2.frequency.setValueAtTime(1318.51, now + 0.1); // E6
      gain2.gain.setValueAtTime(0.25, now + 0.1);
      gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.7);
      osc2.connect(gain2);
      gain2.connect(this.ctx.destination);
      osc2.start(now + 0.1);
      osc2.stop(now + 0.7);
    } catch (e) {
      console.warn("Audio play error", e);
    }
  }
}

const sfx = new SoundFX();

// ==========================================
// 4. HELPER UTILITIES
// ==========================================
function formatIDR(amount) {
  if (isNaN(amount) || amount === null || amount === undefined) return "Rp 0";
  return "Rp " + Math.round(amount).toLocaleString("id-ID");
}

function parseIDR(str) {
  if (typeof str === "number") return str;
  if (!str) return 0;
  const cleaned = str.toString().replace(/[^0-9]/g, "");
  return parseInt(cleaned, 10) || 0;
}

function getFormattedDate(d = new Date()) {
  const day = String(d.getDate()).padStart(2, "0");
  const month = String(d.getMonth() + 1).padStart(2, "0");
  const year = d.getFullYear();
  return `${day}/${month}/${year}`;
}

function getFormattedTime(d = new Date()) {
  const hours = String(d.getHours()).padStart(2, "0");
  const minutes = String(d.getMinutes()).padStart(2, "0");
  const seconds = String(d.getSeconds()).padStart(2, "0");
  return `${hours}:${minutes}:${seconds} WIB`;
}

function getIsoDate(d = new Date()) {
  return d.toISOString().split("T")[0];
}

function showToast(message, icon = "ℹ️") {
  const container = document.getElementById("toastContainer");
  if (!container) return;
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(-20px)";
    setTimeout(() => toast.remove(), 300);
  }, 2800);
}

// Generate New Order ID
function generateOrderId() {
  const now = new Date();
  const d = String(now.getDate()).padStart(2, "0");
  const m = String(now.getMonth() + 1).padStart(2, "0");
  const y = String(now.getFullYear()).slice(-2);
  const seq = String(state.currentOrderNumber).padStart(4, "0");
  return `#KYR-${d}${m}${y}-${seq}`;
}

// ==========================================
// 5. LOCALSTORAGE MANAGEMENT & PRE-SEEDING
// ==========================================
function loadTransactions() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.TRANSACTIONS);
    if (!raw) {
      const initial = generateSampleTransactions();
      localStorage.setItem(STORAGE_KEYS.TRANSACTIONS, JSON.stringify(initial));
      return initial;
    }
    return JSON.parse(raw);
  } catch (e) {
    console.error("Failed to load transactions", e);
    return [];
  }
}

function saveTransactions(transactions) {
  try {
    localStorage.setItem(STORAGE_KEYS.TRANSACTIONS, JSON.stringify(transactions));
    updateReportCounts();
  } catch (e) {
    console.error("Failed to save transactions", e);
  }
}

function loadAdminNotes() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.ADMIN_NOTES);
    if (!raw) {
      const defaultNotes = [
        {
          id: "note-1",
          title: "Modal Kasir Shift Pagi",
          category: "modal",
          content: "Uang modal awal di laci kasir Rp 200.000 (pecahan 5k, 10k, 20k lengkap untuk kembalian).",
          timestamp: "01/10/2026 09:00 WIB"
        },
        {
          id: "note-2",
          title: "Persediaan Saos Mentai & Mozarella",
          category: "stok",
          content: "Stok Saos Mentai aman untuk 50 porsi. Ekstra keju mozarella baru dibuka 1 pack dari chiller.",
          timestamp: "01/10/2026 14:30 WIB"
        },
        {
          id: "note-3",
          title: "Pesan Operasional Shift 1 ke Shift 2",
          category: "shift",
          content: "Cup minuman matcha sudah diisi ulang di bar. Mesin kasir & printer struk berfungsi sangat baik.",
          timestamp: "01/10/2026 17:00 WIB"
        }
      ];
      localStorage.setItem(STORAGE_KEYS.ADMIN_NOTES, JSON.stringify(defaultNotes));
      return defaultNotes;
    }
    return JSON.parse(raw);
  } catch (e) {
    return [];
  }
}

function saveAdminNotes(notes) {
  try {
    localStorage.setItem(STORAGE_KEYS.ADMIN_NOTES, JSON.stringify(notes));
  } catch (e) {
    console.error("Failed to save notes", e);
  }
}

function loadStockState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.MENU_STOCK);
    return raw ? JSON.parse(raw) : {};
  } catch (e) {
    return {};
  }
}

function saveStockState(stockObj) {
  try {
    localStorage.setItem(STORAGE_KEYS.MENU_STOCK, JSON.stringify(stockObj));
  } catch (e) {
    console.error("Failed to save stock state", e);
  }
}

// Generate Realistic Sample Transactions for Today
function generateSampleTransactions() {
  const today = new Date();
  const dateStr = getFormattedDate(today);

  return [
    {
      id: "#KYR-011026-0001",
      date: dateStr,
      time: "11:20:15 WIB",
      isoDate: getIsoDate(today),
      orderType: "Dine In",
      customer: "Kak Naufal",
      table: "01",
      cashier: "Admin Shift 1",
      paymentMethod: "Tunai",
      items: [
        { id: "dm-6", name: "Dimsum Mentai Isi 6", price: 21000, qty: 1, note: "Saus mentai gurih torched" },
        { id: "mat-sig", name: "Signature Matcha", price: 13000, qty: 1, note: "Normal ice" }
      ],
      subtotal: 34000,
      discount: 0,
      total: 34000,
      cashPaid: 50000,
      cashChange: 16000,
      notes: "Pelanggan makan di meja 1"
    },
    {
      id: "#KYR-011026-0002",
      date: dateStr,
      time: "12:45:20 WIB",
      isoDate: getIsoDate(today),
      orderType: "Take Away",
      customer: "Kak Rian",
      table: "-",
      cashier: "Admin Shift 1",
      paymentMethod: "Non-Tunai (QRIS)",
      items: [
        { id: "dhl-6", name: "Dimsum Hot Lava Isi 6", price: 21000, qty: 2, note: "Pedas mantap" },
        { id: "add-moza", name: "Mozarella (Ekstra)", price: 2000, qty: 2, note: "" },
        { id: "cof-aren", name: "Kopi Susu Gula Aren", price: 10000, qty: 2, note: "Less ice" }
      ],
      subtotal: 66000,
      discount: 0,
      total: 66000,
      cashPaid: 66000,
      cashChange: 0,
      notes: "Bungkus rapi saos dipisah"
    },
    {
      id: "#KYR-011026-0003",
      date: dateStr,
      time: "14:10:05 WIB",
      isoDate: getIsoDate(today),
      orderType: "Dine In",
      customer: "Kak Dinda",
      table: "03",
      cashier: "Admin Shift 1",
      paymentMethod: "Tunai",
      items: [
        { id: "dm-10", name: "Dimsum Mentai Isi 10", price: 36000, qty: 1, note: "" },
        { id: "add-chili", name: "Chili Oil", price: 2500, qty: 1, note: "" },
        { id: "mat-latte", name: "Choco Matcha Latte", price: 15000, qty: 1, note: "Ekstra manis" }
      ],
      subtotal: 53500,
      discount: 3500,
      total: 50000,
      cashPaid: 50000,
      cashChange: 0,
      notes: "Voucher Pelanggan Setia"
    },
    {
      id: "#KYR-011026-0004",
      date: dateStr,
      time: "18:30:44 WIB",
      isoDate: getIsoDate(today),
      orderType: "Dine In",
      customer: "Kak Gilang & Teman",
      table: "05",
      cashier: "Admin Shift 1",
      paymentMethod: "Non-Tunai (QRIS)",
      items: [
        { id: "dm-20", name: "Dimsum Mentai Isi 20", price: 68000, qty: 1, note: "Platter jumbo" },
        { id: "dhl-10", name: "Dimsum Hot Lava Isi 10", price: 36000, qty: 1, note: "Pedas ekstra" },
        { id: "cof-aren", name: "Kopi Susu Gula Aren", price: 10000, qty: 2, note: "" },
        { id: "mat-sig", name: "Signature Matcha", price: 13000, qty: 2, note: "" }
      ],
      subtotal: 150000,
      discount: 10000,
      total: 140000,
      cashPaid: 140000,
      cashChange: 0,
      notes: "Meja 5 ramean"
    }
  ];
}

// ==========================================
// 6. INITIALIZATION & APP BOOTSTRAP
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  initLiveClock();
  initSoundPreference();
  initNavigation();
  initCategoryFilter();
  initSearch();
  initCartListeners();
  initPaymentModalListeners();
  initReceiptModalListeners();
  initScrollAnimations();
  initScrollToTop();
  initAdminNotesView();
  initStockManagement();
  
  // Render POS products
  renderProductGrid();
  renderCart();
  
  // Render Reports
  updateReportCounts();
  renderReportsView();

  // Next order sequence calculation
  const txs = loadTransactions();
  state.currentOrderNumber = txs.length + 1;
  document.getElementById("currentOrderId").textContent = generateOrderId();

  // Keyboard shortcut listener
  setupKeyboardShortcuts();
});

// Live Clock
function initLiveClock() {
  const dateEl = document.getElementById("liveDateText");
  const timeEl = document.getElementById("liveTimeText");
  
  function update() {
    const now = new Date();
    const options = { weekday: 'short', day: '2-digit', month: 'short', year: 'numeric' };
    const dateFormatted = now.toLocaleDateString('id-ID', options);
    const timeFormatted = String(now.getHours()).padStart(2, "0") + ":" +
                          String(now.getMinutes()).padStart(2, "0") + ":" +
                          String(now.getSeconds()).padStart(2, "0") + " WIB";
    if (dateEl) dateEl.textContent = dateFormatted;
    if (timeEl) timeEl.textContent = timeFormatted;
  }

  update();
  setInterval(update, 1000);
}

// Sound Preference
function initSoundPreference() {
  const saved = localStorage.getItem(STORAGE_KEYS.SOUND_ENABLED);
  if (saved !== null) {
    state.soundEnabled = saved === "true";
  }
  updateSoundIcon();

  const toggleBtn = document.getElementById("soundToggleBtn");
  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      state.soundEnabled = !state.soundEnabled;
      localStorage.setItem(STORAGE_KEYS.SOUND_ENABLED, state.soundEnabled);
      updateSoundIcon();
      showToast(state.soundEnabled ? "Suara Kasir Diaktifkan 🔊" : "Suara Kasir Dinonaktifkan 🔇", "🔔");
      if (state.soundEnabled) sfx.playBeep();
    });
  }
}

function updateSoundIcon() {
  const iconOn = document.getElementById("soundIconOn");
  const iconOff = document.getElementById("soundIconOff");
  if (!iconOn || !iconOff) return;
  if (state.soundEnabled) {
    iconOn.classList.remove("hidden");
    iconOff.classList.add("hidden");
  } else {
    iconOn.classList.add("hidden");
    iconOff.classList.remove("hidden");
  }
}

// Navigation Tabs
function initNavigation() {
  const tabs = document.querySelectorAll(".nav-tab");
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const target = tab.getAttribute("data-tab");
      switchTab(target);
    });
  });
}

function switchTab(tabName) {
  state.currentTab = tabName;
  document.querySelectorAll(".nav-tab").forEach(t => {
    t.classList.toggle("active", t.getAttribute("data-tab") === tabName);
  });

  const viewPos = document.getElementById("viewPos");
  const viewReports = document.getElementById("viewReports");
  const viewNotes = document.getElementById("viewNotes");

  if (viewPos) viewPos.classList.toggle("active", tabName === "pos");
  if (viewReports) viewReports.classList.toggle("active", tabName === "reports");
  if (viewNotes) viewNotes.classList.toggle("active", tabName === "admin-notes");

  window.scrollTo({ top: 0, behavior: "smooth" });

  if (tabName === "reports") {
    renderReportsView();
  } else if (tabName === "admin-notes") {
    renderAdminNotes();
  }
  sfx.playBeep();
}

// Category Filter Bar & Horizontal Scrolling
function initCategoryFilter() {
  const pills = document.querySelectorAll(".cat-pill");
  pills.forEach(pill => {
    pill.addEventListener("click", () => {
      pills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      const cat = pill.getAttribute("data-cat");
      filterCategory(cat);
    });
  });

  const scrollContainer = document.getElementById("categoryScroll");
  const prevBtn = document.getElementById("catNavPrev");
  const nextBtn = document.getElementById("catNavNext");

  if (prevBtn && scrollContainer) {
    prevBtn.addEventListener("click", () => {
      scrollContainer.scrollBy({ left: -200, behavior: "smooth" });
    });
  }
  if (nextBtn && scrollContainer) {
    nextBtn.addEventListener("click", () => {
      scrollContainer.scrollBy({ left: 200, behavior: "smooth" });
    });
  }
}

function filterCategory(category) {
  state.activeCategory = category;
  document.querySelectorAll(".cat-pill").forEach(p => {
    p.classList.toggle("active", p.getAttribute("data-cat") === category);
  });
  renderProductGrid();
  sfx.playBeep();
}

// Search Filter
function initSearch() {
  const searchInput = document.getElementById("menuSearchInput");
  const clearBtn = document.getElementById("clearSearchBtn");

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      state.searchKeyword = e.target.value.trim().toLowerCase();
      if (clearBtn) {
        clearBtn.classList.toggle("hidden", state.searchKeyword === "");
      }
      renderProductGrid();
    });
  }

  if (clearBtn && searchInput) {
    clearBtn.addEventListener("click", () => {
      searchInput.value = "";
      state.searchKeyword = "";
      clearBtn.classList.add("hidden");
      renderProductGrid();
      searchInput.focus();
    });
  }
}

// Keyboard shortcuts
function setupKeyboardShortcuts() {
  window.addEventListener("keydown", (e) => {
    // F4 -> Pay Now
    if (e.key === "F4") {
      e.preventDefault();
      const payBtn = document.getElementById("btnProcessPayment");
      if (payBtn && !payBtn.disabled) {
        payBtn.click();
      }
    }
    // Search slash or Ctrl+K
    if ((e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") ||
        (e.ctrlKey && e.key === "k")) {
      e.preventDefault();
      const searchInput = document.getElementById("menuSearchInput");
      if (searchInput) {
        searchInput.focus();
        searchInput.select();
      }
    }
    // Esc closes open modals
    if (e.key === "Escape") {
      closeAllModals();
    }
  });
}

function closeAllModals() {
  document.querySelectorAll(".modal-overlay").forEach(m => m.classList.add("hidden"));
}

// ==========================================
// 7. RENDER MENU / PRODUCT GRID
// ==========================================
function renderProductGrid() {
  const container = document.getElementById("productGridContainer");
  const countBadge = document.getElementById("menuCountBadge");
  if (!container) return;

  const stockState = loadStockState();

  // Filter items
  const filtered = MENU_ITEMS.filter(item => {
    // Check Category
    let matchCat = true;
    if (state.activeCategory !== "all") {
      if (state.activeCategory === "makanan") {
        matchCat = item.type === "makanan";
      } else if (state.activeCategory === "minuman") {
        matchCat = item.type === "minuman";
      } else {
        matchCat = item.category === state.activeCategory;
      }
    }

    // Check Search
    let matchSearch = true;
    if (state.searchKeyword) {
      const q = state.searchKeyword;
      matchSearch = item.name.toLowerCase().includes(q) ||
                    item.desc.toLowerCase().includes(q) ||
                    item.category.toLowerCase().includes(q);
    }

    return matchCat && matchSearch;
  });

  if (countBadge) {
    countBadge.textContent = `Menampilkan ${filtered.length} menu`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 3rem 1rem; color: #64748b;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔍</div>
        <h3 style="font-size: 1.2rem; color: #0f172a; margin-bottom: 0.25rem;">Menu Tidak Ditemukan</h3>
        <p>Coba gunakan kata kunci pencarian lain atau pilih kategori Semua Menu.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => {
    const isOutOfStock = stockState[item.id] === false;
    const cartItem = state.cart.find(c => c.id === item.id);
    const cartQty = cartItem ? cartItem.qty : 0;

    // Special badge HTML
    let badgeHtml = "";
    if (item.badge) {
      if (item.badge.type === "mentai-k") {
        badgeHtml = `
          <div class="card-badge-top-left badge-mentai-k">
            <span class="k-emblem-badge">K</span>
            <span>${item.badge.text}</span>
          </div>
        `;
      } else if (item.badge.type === "hotlava-fire") {
        badgeHtml = `
          <div class="card-badge-top-left badge-hotlava-fire">
            <span>${item.badge.text}</span>
          </div>
        `;
      } else {
        badgeHtml = `
          <div class="card-badge-top-left badge-generic">
            <span>${item.badge.text}</span>
          </div>
        `;
      }
    }

    // Out of stock badge
    const stockBadge = isOutOfStock ? `
      <div class="card-badge-stock stock-out">HABIS</div>
    ` : "";

    // Action button / stepper
    let actionBtnHtml = "";
    if (isOutOfStock) {
      actionBtnHtml = `<button type="button" class="btn-add-item" disabled style="background:#cbd5e1;cursor:not-allowed;">Habis</button>`;
    } else if (cartQty > 0) {
      actionBtnHtml = `
        <div class="card-stepper">
          <button type="button" class="step-btn" onclick="updateItemQty('${item.id}', -1)" title="Kurangi">-</button>
          <span class="step-count">${cartQty}</span>
          <button type="button" class="step-btn" onclick="updateItemQty('${item.id}', 1)" title="Tambah">+</button>
        </div>
      `;
    } else {
      actionBtnHtml = `
        <button type="button" class="btn-add-item" onclick="addItemToCart('${item.id}')">
          <span>+ Tambah</span>
        </button>
      `;
    }

    return `
      <article class="product-card ${item.theme} ${isOutOfStock ? 'is-out-of-stock' : ''}" id="card-${item.id}">
        <div class="card-image-wrap">
          <img src="${item.image}" alt="${item.name}" loading="lazy" onerror="this.src='assets/logo_kyaro.png'">
          ${badgeHtml}
          ${stockBadge}
        </div>
        <div class="card-body">
          <span class="card-category-tag">${formatCategoryTag(item.category)}</span>
          <h3 class="card-title">${item.name}</h3>
          <p class="card-desc">${item.desc}</p>
          <div class="card-footer">
            <span class="card-price">${formatIDR(item.price)}</span>
            <div class="card-actions-wrap">
              ${actionBtnHtml}
            </div>
          </div>
        </div>
      </article>
    `;
  }).join("");

  // Re-observe scroll animations
  observeScrollElements();
}

function formatCategoryTag(cat) {
  switch (cat) {
    case "dimsum-mentai": return "🥟 DIMSUM MENTAI (KUNING)";
    case "dimsum-hot-lava": return "🌶️ DIMSUM HOT LAVA (MERAH)";
    case "additional": return "➕ EKSTRA TOPPING";
    case "coffee": return "☕ COFFEE SERIES";
    case "matcha": return "🍵 MATCHA SERIES";
    case "chocolate": return "🍫 CHOCOLATE SERIES";
    default: return cat.toUpperCase();
  }
}

// ==========================================
// 8. CART & ORDER MANAGEMENT
// ==========================================
function initCartListeners() {
  // Clear Cart Button
  const clearBtn = document.getElementById("clearCartBtn");
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (state.cart.length === 0) return;
      if (confirm("Kosongkan semua pesanan di keranjang?")) {
        state.cart = [];
        state.discount.value = 0;
        renderCart();
        renderProductGrid();
        showToast("Keranjang berhasil dikosongkan", "🗑️");
      }
    });
  }

  // Dine In / Take Away Switch
  const dineInBtn = document.getElementById("typeDineInBtn");
  const takeAwayBtn = document.getElementById("typeTakeAwayBtn");
  const tableContainer = document.getElementById("tableFieldContainer");

  if (dineInBtn && takeAwayBtn) {
    dineInBtn.addEventListener("click", () => {
      dineInBtn.classList.add("active");
      takeAwayBtn.classList.remove("active");
      state.orderType = "Dine In";
      if (tableContainer) tableContainer.style.display = "flex";
      sfx.playBeep();
    });

    takeAwayBtn.addEventListener("click", () => {
      takeAwayBtn.classList.add("active");
      dineInBtn.classList.remove("active");
      state.orderType = "Take Away";
      if (tableContainer) tableContainer.style.display = "none";
      sfx.playBeep();
    });
  }

  // Customer Name & Table
  const customerInput = document.getElementById("customerNameInput");
  if (customerInput) {
    customerInput.addEventListener("input", (e) => {
      state.customerName = e.target.value.trim() || "Pelanggan";
    });
  }

  const tableInput = document.getElementById("tableNoInput");
  if (tableInput) {
    tableInput.addEventListener("input", (e) => {
      state.tableNumber = e.target.value.trim() || "-";
    });
  }

  // General note
  const generalNoteInput = document.getElementById("orderGeneralNote");
  if (generalNoteInput) {
    generalNoteInput.addEventListener("input", (e) => {
      state.generalOrderNote = e.target.value.trim();
    });
  }

  // Discount toggle
  const toggleDiscountBtn = document.getElementById("btnToggleDiscount");
  const discountBox = document.getElementById("discountInputBox");
  if (toggleDiscountBtn && discountBox) {
    toggleDiscountBtn.addEventListener("click", () => {
      discountBox.classList.toggle("hidden");
    });
  }

  // Apply discount button
  const applyDiscountBtn = document.getElementById("applyDiscountBtn");
  if (applyDiscountBtn) {
    applyDiscountBtn.addEventListener("click", () => {
      const valInput = document.getElementById("discountValInput");
      const typeSelect = document.getElementById("discountTypeSelect");
      const val = parseFloat(valInput.value) || 0;
      state.discount = {
        type: typeSelect.value,
        value: val
      };
      renderCart();
      showToast("Voucher diskon diterapkan!", "🏷️");
    });
  }

  // Process Payment button (opens payment modal)
  const payBtn = document.getElementById("btnProcessPayment");
  if (payBtn) {
    payBtn.addEventListener("click", () => {
      if (state.cart.length === 0) return;
      openPaymentModal();
    });
  }
}

function addItemToCart(itemId) {
  const product = MENU_ITEMS.find(m => m.id === itemId);
  if (!product) return;

  const existing = state.cart.find(c => c.id === itemId);
  if (existing) {
    existing.qty += 1;
  } else {
    state.cart.push({
      id: product.id,
      name: product.name,
      price: product.price,
      qty: 1,
      image: product.image,
      category: product.category,
      note: ""
    });
  }

  sfx.playBeep();
  renderCart();
  renderProductGrid();
}

function updateItemQty(itemId, delta) {
  const item = state.cart.find(c => c.id === itemId);
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {
    state.cart = state.cart.filter(c => c.id !== itemId);
  }

  sfx.playBeep();
  renderCart();
  renderProductGrid();
}

function removeItemFromCart(itemId) {
  state.cart = state.cart.filter(c => c.id !== itemId);
  sfx.playBeep();
  renderCart();
  renderProductGrid();
}

function calculateTotals() {
  const subtotal = state.cart.reduce((acc, item) => acc + (item.price * item.qty), 0);
  let discountAmount = 0;
  if (state.discount.value > 0) {
    if (state.discount.type === "percent") {
      discountAmount = (subtotal * state.discount.value) / 100;
    } else {
      discountAmount = state.discount.value;
    }
  }
  discountAmount = Math.min(discountAmount, subtotal);
  const total = Math.max(0, subtotal - discountAmount);

  return { subtotal, discountAmount, total };
}

function renderCart() {
  const listEl = document.getElementById("cartItemsList");
  const countEl = document.getElementById("cartItemTotalCount");
  const subtotalEl = document.getElementById("cartSubtotalText");
  const discountEl = document.getElementById("cartDiscountText");
  const totalEl = document.getElementById("cartTotalPriceText");
  const payBtn = document.getElementById("btnProcessPayment");
  if (!listEl) return;

  const totalQty = state.cart.reduce((acc, item) => acc + item.qty, 0);
  const { subtotal, discountAmount, total } = calculateTotals();

  if (countEl) countEl.textContent = totalQty;
  if (subtotalEl) subtotalEl.textContent = formatIDR(subtotal);
  if (discountEl) discountEl.textContent = "- " + formatIDR(discountAmount);
  if (totalEl) totalEl.textContent = formatIDR(total);

  if (payBtn) {
    payBtn.disabled = state.cart.length === 0;
  }

  if (state.cart.length === 0) {
    listEl.innerHTML = `
      <div class="empty-cart-state" id="emptyCartState">
        <div class="empty-icon">🥟</div>
        <h4>Keranjang Masih Kosong</h4>
        <p>Klik menu di samping untuk menambahkan pesanan ke keranjang.</p>
      </div>
    `;
    return;
  }

  listEl.innerHTML = state.cart.map(item => {
    const itemTotal = item.price * item.qty;
    const noteHtml = item.note ? `
      <span class="cart-item-note-text">Catatan: ${item.note}</span>
    ` : "";

    return `
      <div class="cart-item-row" id="cart-row-${item.id}">
        <img src="${item.image}" alt="${item.name}" class="cart-item-thumb" onerror="this.src='assets/logo_kyaro.png'">
        <div class="cart-item-info">
          <h4 class="cart-item-title">${item.name}</h4>
          <div class="cart-item-meta">
            <span>${formatIDR(item.price)}</span>
            <span>•</span>
            <button type="button" class="btn-item-note" onclick="openItemNoteModal('${item.id}')">
              ${item.note ? 'Edit Catatan' : '+ Catatan'}
            </button>
          </div>
          ${noteHtml}
          <div class="cart-item-actions">
            <div class="cart-qty-ctrl">
              <button type="button" class="cart-qty-btn" onclick="updateItemQty('${item.id}', -1)">-</button>
              <span class="cart-qty-num">${item.qty}</span>
              <button type="button" class="cart-qty-btn" onclick="updateItemQty('${item.id}', 1)">+</button>
            </div>
            <span class="cart-item-total">${formatIDR(itemTotal)}</span>
          </div>
        </div>
        <button type="button" class="btn-remove-item" onclick="removeItemFromCart('${item.id}')" title="Hapus menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
        </button>
      </div>
    `;
  }).join("");
}

// ==========================================
// 9. ITEM NOTE MODAL
// ==========================================
function openItemNoteModal(itemId) {
  const item = state.cart.find(c => c.id === itemId);
  if (!item) return;

  state.activeItemNoteId = itemId;
  const modal = document.getElementById("itemNoteModal");
  const title = document.getElementById("noteModalItemTitle");
  const input = document.getElementById("itemNoteInput");

  if (title) title.textContent = `Catatan Menu: ${item.name}`;
  if (input) input.value = item.note || "";

  if (modal) modal.classList.remove("hidden");
  if (input) setTimeout(() => input.focus(), 100);
}

function appendItemNote(text) {
  const input = document.getElementById("itemNoteInput");
  if (!input) return;
  if (input.value) {
    input.value += `, ${text}`;
  } else {
    input.value = text;
  }
}

document.getElementById("btnSaveItemNote")?.addEventListener("click", () => {
  if (!state.activeItemNoteId) return;
  const item = state.cart.find(c => c.id === state.activeItemNoteId);
  const input = document.getElementById("itemNoteInput");
  if (item && input) {
    item.note = input.value.trim();
  }
  document.getElementById("itemNoteModal")?.classList.add("hidden");
  renderCart();
  showToast("Catatan menu disimpan", "📝");
});

document.getElementById("closeNoteModalBtn")?.addEventListener("click", () => {
  document.getElementById("itemNoteModal")?.classList.add("hidden");
});

document.getElementById("btnCancelItemNote")?.addEventListener("click", () => {
  document.getElementById("itemNoteModal")?.classList.add("hidden");
});

// ==========================================
// 10. PAYMENT MODAL LOGIC (TUNAI & NON-TUNAI)
// ==========================================
function initPaymentModalListeners() {
  const modal = document.getElementById("paymentModal");
  const closeBtn = document.getElementById("closePaymentModalBtn");
  const cancelBtn = document.getElementById("btnCancelPayment");
  const confirmBtn = document.getElementById("btnConfirmPayment");
  const tabCash = document.getElementById("tabMethodCash");
  const tabCashless = document.getElementById("tabMethodCashless");
  const cashInput = document.getElementById("cashAmountInput");
  const clearInputBtn = document.getElementById("btnClearCashInput");
  const exactCashBtn = document.getElementById("btnExactCash");

  if (closeBtn) closeBtn.addEventListener("click", () => modal.classList.add("hidden"));
  if (cancelBtn) cancelBtn.addEventListener("click", () => modal.classList.add("hidden"));

  // Switch Method Tabs
  if (tabCash && tabCashless) {
    tabCash.addEventListener("click", () => {
      tabCash.classList.add("active");
      tabCashless.classList.remove("active");
      document.getElementById("panelMethodCash")?.classList.add("active");
      document.getElementById("panelMethodCashless")?.classList.remove("active");
      state.currentPaymentMethod = "Tunai";
      updateConfirmButtonState();
      sfx.playBeep();
    });

    tabCashless.addEventListener("click", () => {
      tabCashless.classList.add("active");
      tabCash.classList.remove("active");
      document.getElementById("panelMethodCashless")?.classList.add("active");
      document.getElementById("panelMethodCash")?.classList.remove("active");
      state.currentPaymentMethod = "Non-Tunai (QRIS)";
      updateConfirmButtonState();
      sfx.playBeep();
    });
  }

  // Cash Amount Input with Real-time Precise Calculation
  if (cashInput) {
    cashInput.addEventListener("input", (e) => {
      const raw = parseIDR(e.target.value);
      state.cashPaidAmount = raw;
      if (raw > 0) {
        cashInput.value = raw.toLocaleString("id-ID");
      } else {
        cashInput.value = "";
      }
      calculateChange();
    });
  }

  if (clearInputBtn && cashInput) {
    clearInputBtn.addEventListener("click", () => {
      cashInput.value = "";
      state.cashPaidAmount = 0;
      calculateChange();
      cashInput.focus();
    });
  }

  // Quick Cash Denomination Buttons
  const quickContainer = document.getElementById("quickCashButtonsContainer");
  if (quickContainer) {
    quickContainer.querySelectorAll(".cash-btn[data-val]").forEach(btn => {
      btn.addEventListener("click", () => {
        const val = parseInt(btn.getAttribute("data-val"), 10);
        state.cashPaidAmount = val;
        if (cashInput) cashInput.value = val.toLocaleString("id-ID");
        calculateChange();
        sfx.playBeep();
      });
    });
  }

  if (exactCashBtn) {
    exactCashBtn.addEventListener("click", () => {
      const { total } = calculateTotals();
      state.cashPaidAmount = total;
      if (cashInput) cashInput.value = total.toLocaleString("id-ID");
      calculateChange();
      sfx.playBeep();
    });
  }

  // Confirm Payment & Complete Transaction
  if (confirmBtn) {
    confirmBtn.addEventListener("click", () => {
      executeCompleteTransaction();
    });
  }
}

function openPaymentModal() {
  const { total } = calculateTotals();
  const modal = document.getElementById("paymentModal");
  const orderIdText = document.getElementById("modalOrderIdText");
  const billAmount = document.getElementById("modalBillAmount");
  const billInfo = document.getElementById("modalBillItemsInfo");
  const qrisAmount = document.getElementById("qrisTotalDisplay");
  const cashInput = document.getElementById("cashAmountInput");

  const orderId = generateOrderId();
  if (orderIdText) orderIdText.textContent = orderId;
  if (billAmount) billAmount.textContent = formatIDR(total);
  if (qrisAmount) qrisAmount.textContent = formatIDR(total);

  const totalQty = state.cart.reduce((acc, item) => acc + item.qty, 0);
  if (billInfo) {
    const cust = state.customerName ? `Pelanggan: ${state.customerName}` : "Pelanggan Umum";
    const tbl = state.orderType === "Dine In" ? `Meja ${state.tableNumber}` : "Bawa Pulang";
    billInfo.textContent = `${totalQty} item • ${state.orderType} (${tbl}) • ${cust}`;
  }

  // Reset to default: Exact cash
  state.cashPaidAmount = total;
  if (cashInput) cashInput.value = total.toLocaleString("id-ID");
  calculateChange();

  if (modal) modal.classList.remove("hidden");
  if (cashInput) setTimeout(() => cashInput.select(), 150);
}

function calculateChange() {
  const { total } = calculateTotals();
  const paid = state.cashPaidAmount;
  const billValEl = document.getElementById("calcBillVal");
  const paidValEl = document.getElementById("calcPaidVal");
  const resultLabelEl = document.getElementById("calcResultLabel");
  const resultValEl = document.getElementById("calcResultVal");
  const warningMsgEl = document.getElementById("calcWarningMsg");

  if (billValEl) billValEl.textContent = formatIDR(total);
  if (paidValEl) paidValEl.textContent = formatIDR(paid);

  const diff = paid - total;

  if (diff >= 0) {
    // Exact or change
    if (resultLabelEl) resultLabelEl.textContent = "Kembalian:";
    if (resultValEl) {
      resultValEl.textContent = formatIDR(diff);
      resultValEl.className = "calc-result-val text-green";
    }
    if (warningMsgEl) warningMsgEl.classList.add("hidden");
  } else {
    // Insufficient cash
    const shortage = Math.abs(diff);
    if (resultLabelEl) resultLabelEl.textContent = "Uang Kurang:";
    if (resultValEl) {
      resultValEl.textContent = "- " + formatIDR(shortage);
      resultValEl.className = "calc-result-val text-danger";
    }
    if (warningMsgEl) {
      warningMsgEl.textContent = `⚠️ Uang yang dimasukkan masih kurang ${formatIDR(shortage)}! Silakan masukkan nominal yang cukup.`;
      warningMsgEl.classList.remove("hidden");
    }
  }

  updateConfirmButtonState();
}

function updateConfirmButtonState() {
  const confirmBtn = document.getElementById("btnConfirmPayment");
  const { total } = calculateTotals();
  if (!confirmBtn) return;

  if (state.currentPaymentMethod === "Tunai") {
    const isSufficient = state.cashPaidAmount >= total;
    confirmBtn.disabled = !isSufficient;
  } else {
    // Non-tunai QRIS is always ready to confirm
    confirmBtn.disabled = false;
  }
}

// Complete Order Transaction Execution
function executeCompleteTransaction() {
  const { subtotal, discountAmount, total } = calculateTotals();
  const now = new Date();
  const orderId = generateOrderId();
  const isCash = state.currentPaymentMethod === "Tunai";
  const cashPaid = isCash ? state.cashPaidAmount : total;
  const cashChange = isCash ? Math.max(0, state.cashPaidAmount - total) : 0;

  const newTransaction = {
    id: orderId,
    date: getFormattedDate(now),
    time: getFormattedTime(now),
    isoDate: getIsoDate(now),
    orderType: state.orderType,
    customer: state.customerName,
    table: state.orderType === "Dine In" ? state.tableNumber : "-",
    cashier: "Admin Shift 1",
    paymentMethod: state.currentPaymentMethod,
    items: state.cart.map(c => ({
      id: c.id,
      name: c.name,
      price: c.price,
      qty: c.qty,
      note: c.note || ""
    })),
    subtotal: subtotal,
    discount: discountAmount,
    total: total,
    cashPaid: cashPaid,
    cashChange: cashChange,
    notes: state.generalOrderNote || ""
  };

  // Save to LocalStorage
  const transactions = loadTransactions();
  transactions.unshift(newTransaction);
  saveTransactions(transactions);

  // Play cash register sound
  sfx.playCashRegister();

  // Close payment modal
  document.getElementById("paymentModal")?.classList.add("hidden");

  // Show Toast
  showToast(`Transaksi ${orderId} Berhasil Disimpan!`, "✅");

  // Open Receipt Modal
  openReceiptModal(newTransaction);

  // Reset Cart & Increment Order Sequence
  state.cart = [];
  state.discount.value = 0;
  state.generalOrderNote = "";
  state.currentOrderNumber += 1;
  document.getElementById("currentOrderId").textContent = generateOrderId();
  document.getElementById("orderGeneralNote").value = "";

  renderCart();
  renderProductGrid();
  renderReportsView();
}

// ==========================================
// 11. RECEIPT / STRUK BELANJA MODAL & PRINT
// ==========================================
function initReceiptModalListeners() {
  const modal = document.getElementById("receiptModal");
  const closeBtn = document.getElementById("closeReceiptModalBtn");
  const printBtn = document.getElementById("btnPrintReceiptBtn");
  const newOrderBtn = document.getElementById("btnNewOrderBtn");

  if (closeBtn) closeBtn.addEventListener("click", () => modal.classList.add("hidden"));
  if (newOrderBtn) {
    newOrderBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
      switchTab("pos");
    });
  }

  if (printBtn) {
    printBtn.addEventListener("click", () => {
      window.print();
    });
  }
}

function openReceiptModal(tx) {
  const modal = document.getElementById("receiptModal");
  if (!modal) return;

  // Fill Header Data
  document.getElementById("receiptOrderId").textContent = tx.id;
  document.getElementById("receiptDateTime").textContent = `${tx.date} ${tx.time}`;
  document.getElementById("receiptCashier").textContent = tx.cashier;
  document.getElementById("receiptCustomer").textContent = `${tx.customer} (Meja ${tx.table})`;
  document.getElementById("receiptOrderType").textContent = tx.orderType;

  // Fill Items
  const itemsContainer = document.getElementById("receiptItemsBody");
  if (itemsContainer) {
    itemsContainer.innerHTML = tx.items.map(item => {
      const itemSub = item.price * item.qty;
      const noteHtml = item.note ? `<div class="receipt-item-note-row">↳ ${item.note}</div>` : "";
      return `
        <div>
          <div class="receipt-item-row-receipt">
            <span class="col-item">${item.name}</span>
            <span class="col-qty">x${item.qty}</span>
            <span class="col-price">${formatIDR(item.price)}</span>
            <span class="col-total">${formatIDR(itemSub)}</span>
          </div>
          ${noteHtml}
        </div>
      `;
    }).join("");
  }

  // Fill Calculations
  document.getElementById("receiptSubtotal").textContent = formatIDR(tx.subtotal);
  const discountRow = document.getElementById("receiptDiscountRow");
  if (discountRow) {
    if (tx.discount > 0) {
      discountRow.style.display = "flex";
      document.getElementById("receiptDiscount").textContent = "- " + formatIDR(tx.discount);
    } else {
      discountRow.style.display = "none";
    }
  }

  document.getElementById("receiptGrandTotal").textContent = formatIDR(tx.total);
  document.getElementById("receiptPaymentMethod").textContent = tx.paymentMethod.toUpperCase();
  document.getElementById("receiptCashPaid").textContent = formatIDR(tx.cashPaid);
  document.getElementById("receiptCashChange").textContent = formatIDR(tx.cashChange);

  modal.classList.remove("hidden");
}

// ==========================================
// 12. DATA LAPORAN (THE REQUESTED DATA PEMBELIAN CARD)
// ==========================================
function updateReportCounts() {
  const txs = loadTransactions();
  const countBadge = document.getElementById("navReportCount");
  if (countBadge) {
    countBadge.textContent = txs.length;
  }
}

function renderReportsView() {
  const transactions = loadTransactions();
  const filter = state.reportFilter;

  // Update dynamic card title with current date
  const reportCardTitle = document.getElementById("reportCardTitle");
  const todayDateStr = getFormattedDate(new Date());

  // Filter transactions
  const filtered = transactions.filter(tx => {
    // Date filter
    const todayIso = getIsoDate(new Date());
    const txIso = tx.isoDate || getIsoDate(new Date());

    if (filter.period === "today") {
      if (txIso !== todayIso && tx.date !== todayDateStr) return false;
    } else if (filter.period === "yesterday") {
      const yest = new Date();
      yest.setDate(yest.getDate() - 1);
      const yestIso = getIsoDate(yest);
      if (txIso !== yestIso) return false;
    } else if (filter.period === "week") {
      const weekAgo = new Date();
      weekAgo.setDate(weekAgo.getDate() - 7);
      const weekIso = getIsoDate(weekAgo);
      if (txIso < weekIso) return false;
    } else if (filter.period === "custom" && filter.customDate) {
      if (txIso !== filter.customDate) return false;
    }

    // Payment Method filter
    if (filter.paymentMethod !== "all") {
      if (filter.paymentMethod === "Tunai" && !tx.paymentMethod.includes("Tunai")) return false;
      if (filter.paymentMethod === "Non-Tunai" && !tx.paymentMethod.includes("Non-Tunai")) return false;
    }

    // Search query
    if (filter.search) {
      const q = filter.search.toLowerCase();
      const matchId = tx.id.toLowerCase().includes(q);
      const matchCustomer = tx.customer.toLowerCase().includes(q);
      const matchItem = tx.items.some(i => i.name.toLowerCase().includes(q));
      if (!matchId && !matchCustomer && !matchItem) return false;
    }

    return true;
  });

  // Dynamic Card Title based on period
  if (reportCardTitle) {
    if (filter.period === "today") {
      reportCardTitle.textContent = `DATA PEMBELIAN ${todayDateStr}`;
    } else if (filter.period === "yesterday") {
      const yest = new Date();
      yest.setDate(yest.getDate() - 1);
      reportCardTitle.textContent = `DATA PEMBELIAN ${getFormattedDate(yest)} (KEMARIN)`;
    } else if (filter.period === "week") {
      reportCardTitle.textContent = `DATA PEMBELIAN 7 HARI TERAKHIR`;
    } else if (filter.period === "custom" && filter.customDate) {
      const parts = filter.customDate.split("-");
      const d = `${parts[2]}/${parts[1]}/${parts[0]}`;
      reportCardTitle.textContent = `DATA PEMBELIAN ${d}`;
    } else {
      reportCardTitle.textContent = `DATA PEMBELIAN KESELURUHAN (${filtered.length} TRANSAKSI)`;
    }
  }

  // Calculate KPIs
  const totalRevenue = filtered.reduce((acc, tx) => acc + tx.total, 0);
  const totalOrders = filtered.length;
  const cashTxs = filtered.filter(tx => tx.paymentMethod.includes("Tunai"));
  const nonCashTxs = filtered.filter(tx => tx.paymentMethod.includes("Non-Tunai") || tx.paymentMethod.includes("QRIS"));

  const totalCash = cashTxs.reduce((acc, tx) => acc + tx.total, 0);
  const totalNonCash = nonCashTxs.reduce((acc, tx) => acc + tx.total, 0);

  // Update KPI Cards
  document.getElementById("kpiTotalRevenue").textContent = formatIDR(totalRevenue);
  document.getElementById("kpiTotalOrders").textContent = `${totalOrders} Pesanan`;
  document.getElementById("kpiTotalCash").textContent = formatIDR(totalCash);
  document.getElementById("kpiCashCount").textContent = `${cashTxs.length} transaksi tunai`;
  document.getElementById("kpiTotalNonCash").textContent = formatIDR(totalNonCash);
  document.getElementById("kpiNonCashCount").textContent = `${nonCashTxs.length} transaksi non-tunai`;

  // Render Transaction Cards inside the Main Card
  const listContainer = document.getElementById("transactionsCardsList");
  const countText = document.getElementById("filteredTransactionsCount");
  if (countText) {
    countText.textContent = `Menampilkan ${filtered.length} Transaksi`;
  }

  if (listContainer) {
    if (filtered.length === 0) {
      listContainer.innerHTML = `
        <div style="text-align: center; padding: 3rem 1rem; color: #64748b;">
          <div style="font-size: 3rem; margin-bottom: 0.5rem;">📋</div>
          <h3 style="font-size: 1.15rem; color: #0f172a; margin-bottom: 0.25rem;">Tidak Ada Data Transaksi</h3>
          <p>Belum ada riwayat pembelian untuk filter yang dipilih.</p>
        </div>
      `;
    } else {
      listContainer.innerHTML = filtered.map(tx => {
        const isCash = tx.paymentMethod.includes("Tunai");
        const paymentBadge = isCash ? `
          <span class="tx-badge-payment is-cash">💵 Tunai (Cash)</span>
        ` : `
          <span class="tx-badge-payment is-qris">📱 Non-Tunai (QRIS)</span>
        `;

        const itemsPills = tx.items.map(item => `
          <div class="tx-item-pill">
            <span class="tx-item-name">
              <strong class="tx-item-qty">${item.qty}x</strong> ${item.name}
            </span>
            <span class="tx-item-cost">${formatIDR(item.price * item.qty)}</span>
          </div>
        `).join("");

        return `
          <div class="tx-card" id="tx-card-${tx.id}">
            <div class="tx-card-top">
              <div class="tx-id-group">
                <span class="tx-id">${tx.id}</span>
                <span class="tx-badge-status">✓ Selesai & Lunas</span>
                <span class="tx-badge-type">${tx.orderType}</span>
                ${paymentBadge}
              </div>
              <div class="tx-time-meta">
                <span>📅 ${tx.date}</span>
                <span>•</span>
                <span>⏰ ${tx.time}</span>
              </div>
            </div>

            <!-- Products List Breakdown -->
            <div class="tx-products-box">
              <div class="tx-items-grid">
                ${itemsPills}
              </div>
              ${tx.notes ? `<div style="font-size: 0.75rem; color: #ea580c; margin-top: 0.5rem;">📝 <strong>Catatan:</strong> ${tx.notes}</div>` : ''}
            </div>

            <!-- Bottom Money & Actions -->
            <div class="tx-card-bottom">
              <div class="tx-money-breakdown">
                <div class="tx-money-item">
                  <span class="tx-money-lbl">Pelanggan:</span>
                  <span class="tx-money-val">${tx.customer} (Meja ${tx.table})</span>
                </div>
                <div class="tx-money-item">
                  <span class="tx-money-lbl">Uang Diterima:</span>
                  <span class="tx-money-val">${formatIDR(tx.cashPaid)}</span>
                </div>
                <div class="tx-money-item">
                  <span class="tx-money-lbl">Kembalian:</span>
                  <span class="tx-money-val text-green">${formatIDR(tx.cashChange)}</span>
                </div>
                <div class="tx-money-item">
                  <span class="tx-money-lbl">TOTAL TRANSAKSI:</span>
                  <span class="tx-total-val">${formatIDR(tx.total)}</span>
                </div>
              </div>

              <div class="tx-actions">
                <button type="button" class="btn-tx-action btn-tx-print" onclick="reprintReceipt('${tx.id}')">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
                  <span>Cetak Struk</span>
                </button>
                <button type="button" class="btn-tx-action btn-tx-delete" onclick="deleteTransaction('${tx.id}')" title="Hapus transaksi ini">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
                </button>
              </div>
            </div>
          </div>
        `;
      }).join("");
    }
  }

  // Render Top Items List
  renderTopItems(filtered);

  // Render Payment Ratio
  renderPaymentRatio(totalCash, totalNonCash, totalRevenue);
}

function renderTopItems(transactions) {
  const container = document.getElementById("topItemsList");
  const countBadge = document.getElementById("topItemsCountBadge");
  if (!container) return;

  const itemMap = {};
  transactions.forEach(tx => {
    tx.items.forEach(item => {
      if (!itemMap[item.name]) {
        itemMap[item.name] = { name: item.name, qty: 0, revenue: 0 };
      }
      itemMap[item.name].qty += item.qty;
      itemMap[item.name].revenue += (item.price * item.qty);
    });
  });

  const sorted = Object.values(itemMap).sort((a, b) => b.qty - a.qty);

  if (countBadge) {
    countBadge.textContent = `${sorted.length} Menu Terjual`;
  }

  if (sorted.length === 0) {
    container.innerHTML = `<p style="font-size:0.82rem;color:#64748b;">Belum ada penjualan menu pada periode ini.</p>`;
    return;
  }

  container.innerHTML = sorted.slice(0, 6).map((item, idx) => `
    <div class="top-item-row">
      <div style="display: flex; align-items: center;">
        <span class="top-item-rank">${idx + 1}</span>
        <div class="top-item-meta">
          <span class="top-item-name">${item.name}</span>
          <span class="top-item-qty">Terjual: ${item.qty} porsi / cup</span>
        </div>
      </div>
      <span class="top-item-revenue">${formatIDR(item.revenue)}</span>
    </div>
  `).join("");
}

function renderPaymentRatio(cash, nonCash, total) {
  const container = document.getElementById("paymentRatioContent");
  if (!container) return;

  if (total === 0) {
    container.innerHTML = `<p style="font-size:0.82rem;color:#64748b;">Belum ada data transaksi untuk dihitung.</p>`;
    return;
  }

  const cashPct = Math.round((cash / total) * 100);
  const nonCashPct = 100 - cashPct;

  container.innerHTML = `
    <div class="ratio-bar-wrapper">
      <div class="ratio-bar-track">
        <div class="ratio-bar-cash" style="width: ${cashPct}%" title="Tunai: ${cashPct}%"></div>
        <div class="ratio-bar-qris" style="width: ${nonCashPct}%" title="QRIS: ${nonCashPct}%"></div>
      </div>
      <div class="ratio-legend">
        <span class="legend-cash">💵 Tunai: ${formatIDR(cash)} (${cashPct}%)</span>
        <span class="legend-qris">📱 Non-Tunai: ${formatIDR(nonCash)} (${nonCashPct}%)</span>
      </div>
    </div>
  `;
}

// Reports Filter Listeners
document.querySelectorAll(".date-pill").forEach(pill => {
  pill.addEventListener("click", () => {
    document.querySelectorAll(".date-pill").forEach(p => p.classList.remove("active"));
    pill.classList.add("active");
    state.reportFilter.period = pill.getAttribute("data-period");
    state.reportFilter.customDate = null;
    const customInput = document.getElementById("customDateFilterInput");
    if (customInput) customInput.value = "";
    renderReportsView();
    sfx.playBeep();
  });
});

document.getElementById("customDateFilterInput")?.addEventListener("change", (e) => {
  if (e.target.value) {
    document.querySelectorAll(".date-pill").forEach(p => p.classList.remove("active"));
    state.reportFilter.period = "custom";
    state.reportFilter.customDate = e.target.value;
    renderReportsView();
    sfx.playBeep();
  }
});

document.getElementById("filterPaymentMethod")?.addEventListener("change", (e) => {
  state.reportFilter.paymentMethod = e.target.value;
  renderReportsView();
});

document.getElementById("reportSearchInput")?.addEventListener("input", (e) => {
  state.reportFilter.search = e.target.value.trim();
  renderReportsView();
});

// Action: Reprint Receipt
function reprintReceipt(txId) {
  const transactions = loadTransactions();
  const tx = transactions.find(t => t.id === txId);
  if (tx) {
    openReceiptModal(tx);
    sfx.playBeep();
  }
}

// Action: Delete Single Transaction
function deleteTransaction(txId) {
  if (!confirm(`Hapus data transaksi ${txId}? Tindakan ini tidak dapat dibatalkan.`)) return;
  let transactions = loadTransactions();
  transactions = transactions.filter(t => t.id !== txId);
  saveTransactions(transactions);
  renderReportsView();
  showToast(`Transaksi ${txId} berhasil dihapus`, "🗑️");
}

// Action: Reset All Transactions
document.getElementById("btnResetAllTransactions")?.addEventListener("click", () => {
  if (confirm("Apakah Anda yakin ingin MENGOSONGKAN SELURUH DATA TRANSAKSI untuk memulai shift baru?")) {
    saveTransactions([]);
    renderReportsView();
    showToast("Seluruh data laporan berhasil dikosongkan untuk shift baru", "🧹");
  }
});

// Action: Export to CSV (Excel Ready)
document.getElementById("btnExportCSV")?.addEventListener("click", () => {
  const transactions = loadTransactions();
  if (transactions.length === 0) {
    alert("Tidak ada data transaksi untuk diexport.");
    return;
  }

  let csvContent = "\uFEFF"; // UTF-8 BOM for Excel
  csvContent += "ID Transaksi,Tanggal,Waktu,Tipe Order,Pelanggan,Meja,Kasir,Metode Pembayaran,Rincian Produk,Subtotal,Diskon,Total,Uang Diterima,Kembalian,Catatan\n";

  transactions.forEach(tx => {
    const itemsFormatted = tx.items.map(i => `${i.qty}x ${i.name}`).join(" | ");
    const row = [
      `"${tx.id}"`,
      `"${tx.date}"`,
      `"${tx.time}"`,
      `"${tx.orderType}"`,
      `"${tx.customer}"`,
      `"${tx.table}"`,
      `"${tx.cashier}"`,
      `"${tx.paymentMethod}"`,
      `"${itemsFormatted}"`,
      tx.subtotal,
      tx.discount,
      tx.total,
      tx.cashPaid,
      tx.cashChange,
      `"${tx.notes || ''}"`
    ];
    csvContent += row.join(",") + "\n";
  });

  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  const today = getIsoDate(new Date());
  link.setAttribute("href", url);
  link.setAttribute("download", `LAPORAN_PEMBELIAN_KYARO_${today}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  showToast("File Excel/CSV berhasil diunduh!", "📥");
});

// Action: Print Report Summary
document.getElementById("btnPrintReportSummary")?.addEventListener("click", () => {
  window.print();
});

// ==========================================
// 13. VIEW 3: ADMIN NOTES & SHIFT LOGBOOK
// ==========================================
function initAdminNotesView() {
  const addBtn = document.getElementById("btnOpenNewNoteModal");
  const modal = document.getElementById("newAdminNoteModal");
  const closeBtn = document.getElementById("closeAdminNoteModalBtn");
  const cancelBtn = document.getElementById("btnCancelAdminNote");
  const saveBtn = document.getElementById("btnSaveAdminNote");

  if (addBtn && modal) {
    addBtn.addEventListener("click", () => {
      document.getElementById("adminNoteTitleInput").value = "";
      document.getElementById("adminNoteContentInput").value = "";
      modal.classList.remove("hidden");
    });
  }

  if (closeBtn && modal) closeBtn.addEventListener("click", () => modal.classList.add("hidden"));
  if (cancelBtn && modal) cancelBtn.addEventListener("click", () => modal.classList.add("hidden"));

  if (saveBtn) {
    saveBtn.addEventListener("click", () => {
      const title = document.getElementById("adminNoteTitleInput").value.trim();
      const cat = document.getElementById("adminNoteCategorySelect").value;
      const content = document.getElementById("adminNoteContentInput").value.trim();

      if (!title || !content) {
        alert("Harap isi judul dan konten catatan.");
        return;
      }

      const notes = loadAdminNotes();
      const newNote = {
        id: "note-" + Date.now(),
        title: title,
        category: cat,
        content: content,
        timestamp: `${getFormattedDate(new Date())} ${getFormattedTime(new Date())}`
      };

      notes.unshift(newNote);
      saveAdminNotes(notes);
      modal.classList.add("hidden");
      renderAdminNotes();
      showToast("Catatan admin berhasil ditambahkan", "📌");
      sfx.playBeep();
    });
  }
}

function renderAdminNotes() {
  const container = document.getElementById("adminNotesGrid");
  if (!container) return;

  const notes = loadAdminNotes();
  if (notes.length === 0) {
    container.innerHTML = `<p style="color:#64748b;">Belum ada catatan admin.</p>`;
    return;
  }

  container.innerHTML = notes.map(note => {
    let catTag = "Catatan Umum";
    if (note.category === "modal") catTag = "💵 Uang Modal / Kas";
    if (note.category === "stok") catTag = "📦 Stok & Persediaan";
    if (note.category === "shift") catTag = "🔄 Serah Terima Shift";
    if (note.category === "pelanggan") catTag = "⭐ Pelanggan Khusus";

    return `
      <div class="note-sticky-card cat-${note.category}">
        <div class="note-sticky-top">
          <span class="note-cat-tag">${catTag}</span>
          <span class="note-time">${note.timestamp}</span>
        </div>
        <h3 class="note-card-title">${note.title}</h3>
        <p class="note-card-body">${note.content}</p>
        <div class="note-sticky-footer">
          <button type="button" class="btn-delete-note" onclick="deleteAdminNote('${note.id}')">
            🗑️ Hapus Catatan
          </button>
        </div>
      </div>
    `;
  }).join("");
}

function deleteAdminNote(noteId) {
  if (!confirm("Hapus catatan ini?")) return;
  let notes = loadAdminNotes();
  notes = notes.filter(n => n.id !== noteId);
  saveAdminNotes(notes);
  renderAdminNotes();
  showToast("Catatan berhasil dihapus", "🗑️");
}

// Menu Stock Availability Management
function initStockManagement() {
  const listContainer = document.getElementById("stockToggleList");
  if (!listContainer) return;

  const stockState = loadStockState();

  listContainer.innerHTML = MENU_ITEMS.map(item => {
    const isAvail = stockState[item.id] !== false;
    const btnClass = isAvail ? "status-available" : "status-soldout";
    const btnText = isAvail ? "Tersedia ✓" : "Habis ✕";

    return `
      <div class="stock-item-row">
        <div class="stock-item-info">
          <span>${item.name}</span>
        </div>
        <button type="button" class="stock-switch-btn ${btnClass}" onclick="toggleMenuStock('${item.id}', this)">
          ${btnText}
        </button>
      </div>
    `;
  }).join("");
}

function toggleMenuStock(itemId, btnEl) {
  const stockState = loadStockState();
  const current = stockState[itemId] !== false;
  const updated = !current;
  stockState[itemId] = updated;
  saveStockState(stockState);

  if (updated) {
    btnEl.className = "stock-switch-btn status-available";
    btnEl.textContent = "Tersedia ✓";
    showToast("Menu ditandai Tersedia", "✅");
  } else {
    btnEl.className = "stock-switch-btn status-soldout";
    btnEl.textContent = "Habis ✕";
    showToast("Menu ditandai Habis", "⚠️");
  }

  renderProductGrid();
}

// ==========================================
// 14. SMOOTH SCROLL & REPEATING ANIMATIONS
// ==========================================
function initScrollAnimations() {
  observeScrollElements();
}

function observeScrollElements() {
  const cards = document.querySelectorAll(".product-card, .promo-banner, .report-main-card, .kpi-card");
  
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
        } else {
          // Keep subtle transition so scrolling up or down feels alive and smooth
          entry.target.style.opacity = "0.96";
        }
      });
    }, {
      threshold: 0.05,
      rootMargin: "0px 0px -20px 0px"
    });

    cards.forEach(el => observer.observe(el));
  }
}

function initScrollToTop() {
  const topBtn = document.getElementById("scrollToTopBtn");
  if (!topBtn) return;

  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      topBtn.classList.remove("hidden");
    } else {
      topBtn.classList.add("hidden");
    }
  });

  topBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}
