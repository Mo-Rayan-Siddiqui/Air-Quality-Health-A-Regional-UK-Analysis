// ═══════════════════════════════════════════════════════
// AIR QUALITY & HEALTH — INTERACTIVE CHARTS (Plotly.js)
// ═══════════════════════════════════════════════════════

const DATA = [
  {region:"London",year:2015,admissions:132735,pop:9000000,rate:1474.84,pm25:12.75,no2:31.59,o3:42.82},
  {region:"North West",year:2015,admissions:116295,pop:7300000,rate:1593.09,pm25:10.96,no2:26.94,o3:42.86},
  {region:"Midlands",year:2015,admissions:165497,pop:10800000,rate:1532.38,pm25:11.59,no2:30.51,o3:41.21},
  {region:"East of England",year:2015,admissions:85321,pop:6200000,rate:1376.15,pm25:9.77,no2:23.5,o3:43.95},
  {region:"South East",year:2015,admissions:113922,pop:9200000,rate:1238.29,pm25:10.12,no2:21.48,o3:39.64},
  {region:"South West",year:2015,admissions:66544,pop:5600000,rate:1188.29,pm25:7.72,no2:17.27,o3:49.36},
  {region:"North East and Yorkshire",year:2015,admissions:131945,pop:8100000,rate:1628.96,pm25:9.35,no2:20.54,o3:50.38},
  {region:"London",year:2016,admissions:131995,pop:9000000,rate:1466.62,pm25:12.14,no2:30.48,o3:37.52},
  {region:"North West",year:2016,admissions:113334,pop:7300000,rate:1552.53,pm25:9.72,no2:24.53,o3:41.96},
  {region:"Midlands",year:2016,admissions:162499,pop:10800000,rate:1504.63,pm25:10.77,no2:25.73,o3:42.97},
  {region:"East of England",year:2016,admissions:77954,pop:6200000,rate:1257.33,pm25:9.01,no2:26.23,o3:46.45},
  {region:"South East",year:2016,admissions:111132,pop:9200000,rate:1207.96,pm25:9.27,no2:24.82,o3:42.43},
  {region:"South West",year:2016,admissions:66869,pop:5600000,rate:1194.1,pm25:7.94,no2:15.94,o3:44.1},
  {region:"North East and Yorkshire",year:2016,admissions:115917,pop:8100000,rate:1431.09,pm25:9.7,no2:25.73,o3:45.96},
  {region:"London",year:2017,admissions:118822,pop:9000000,rate:1320.25,pm25:11.94,no2:29.25,o3:37.65},
  {region:"North West",year:2017,admissions:111243,pop:7300000,rate:1523.89,pm25:9.43,no2:22.66,o3:49.02},
  {region:"Midlands",year:2017,admissions:151670,pop:10800000,rate:1404.36,pm25:10.54,no2:22.82,o3:45.16},
  {region:"East of England",year:2017,admissions:79156,pop:6200000,rate:1276.71,pm25:8.93,no2:20.96,o3:48.44},
  {region:"South East",year:2017,admissions:107373,pop:9200000,rate:1167.1,pm25:10.12,no2:27.15,o3:42.31},
  {region:"South West",year:2017,admissions:61229,pop:5600000,rate:1093.38,pm25:7.53,no2:19.48,o3:51.64},
  {region:"North East and Yorkshire",year:2017,admissions:127719,pop:8100000,rate:1576.78,pm25:9.17,no2:22.55,o3:42.93},
  {region:"London",year:2018,admissions:123611,pop:9000000,rate:1373.46,pm25:11.15,no2:29.5,o3:47.34},
  {region:"North West",year:2018,admissions:111790,pop:7300000,rate:1531.38,pm25:9.55,no2:25.89,o3:46.76},
  {region:"Midlands",year:2018,admissions:147016,pop:10800000,rate:1361.26,pm25:9.83,no2:25.3,o3:49.87},
  {region:"East of England",year:2018,admissions:75285,pop:6200000,rate:1214.28,pm25:8.91,no2:25.41,o3:38.77},
  {region:"South East",year:2018,admissions:110335,pop:9200000,rate:1199.3,pm25:9.81,no2:24.7,o3:44.39},
  {region:"South West",year:2018,admissions:60953,pop:5600000,rate:1088.45,pm25:7.57,no2:14.94,o3:47.99},
  {region:"North East and Yorkshire",year:2018,admissions:121421,pop:8100000,rate:1499.03,pm25:9.39,no2:26.43,o3:44.36},
  {region:"London",year:2019,admissions:119967,pop:9000000,rate:1332.97,pm25:11.1,no2:26.74,o3:46.1},
  {region:"North West",year:2019,admissions:108727,pop:7300000,rate:1489.42,pm25:9.55,no2:22.81,o3:47.22},
  {region:"Midlands",year:2019,admissions:149030,pop:10800000,rate:1379.91,pm25:9.98,no2:26.9,o3:42.92},
  {region:"East of England",year:2019,admissions:81506,pop:6200000,rate:1314.61,pm25:8.58,no2:20.66,o3:42.75},
  {region:"South East",year:2019,admissions:108037,pop:9200000,rate:1174.33,pm25:9.35,no2:23.89,o3:45.99},
  {region:"South West",year:2019,admissions:60206,pop:5600000,rate:1075.11,pm25:7.24,no2:15.28,o3:47.87},
  {region:"North East and Yorkshire",year:2019,admissions:121348,pop:8100000,rate:1498.13,pm25:8.84,no2:20.51,o3:46.25},
  {region:"London",year:2020,admissions:97111,pop:9000000,rate:1079.02,pm25:11.45,no2:32.4,o3:43.35},
  {region:"North West",year:2020,admissions:92596,pop:7300000,rate:1268.44,pm25:9.31,no2:23.12,o3:40.28},
  {region:"Midlands",year:2020,admissions:116790,pop:10800000,rate:1081.39,pm25:9.71,no2:24.39,o3:52.83},
  {region:"East of England",year:2020,admissions:59254,pop:6200000,rate:955.72,pm25:8.45,no2:21.74,o3:47.22},
  {region:"South East",year:2020,admissions:91324,pop:9200000,rate:992.66,pm25:8.42,no2:23.32,o3:49.63},
  {region:"South West",year:2020,admissions:54903,pop:5600000,rate:980.42,pm25:7.6,no2:17.17,o3:52.82},
  {region:"North East and Yorkshire",year:2020,admissions:99407,pop:8100000,rate:1227.26,pm25:8.12,no2:21.47,o3:54.39},
  {region:"London",year:2021,admissions:100421,pop:9000000,rate:1115.79,pm25:10.5,no2:25.13,o3:44.54},
  {region:"North West",year:2021,admissions:89245,pop:7300000,rate:1222.54,pm25:8.72,no2:18.71,o3:47.12},
  {region:"Midlands",year:2021,admissions:117322,pop:10800000,rate:1086.32,pm25:8.97,no2:23.38,o3:43.78},
  {region:"East of England",year:2021,admissions:60112,pop:6200000,rate:969.56,pm25:9.13,no2:21.27,o3:45.33},
  {region:"South East",year:2021,admissions:86833,pop:9200000,rate:943.84,pm25:9.21,no2:20.56,o3:46.87},
  {region:"South West",year:2021,admissions:54939,pop:5600000,rate:981.06,pm25:7.69,no2:16.02,o3:49.01},
  {region:"North East and Yorkshire",year:2021,admissions:98504,pop:8100000,rate:1216.11,pm25:8.75,no2:23.45,o3:43.16},
  {region:"London",year:2022,admissions:108863,pop:9000000,rate:1209.6,pm25:10.09,no2:26.27,o3:45.76},
  {region:"North West",year:2022,admissions:105718,pop:7300000,rate:1448.2,pm25:8.9,no2:22.94,o3:44.61},
  {region:"Midlands",year:2022,admissions:142910,pop:10800000,rate:1323.25,pm25:9.4,no2:24.1,o3:43.75},
  {region:"East of England",year:2022,admissions:70038,pop:6200000,rate:1129.65,pm25:9.1,no2:23.7,o3:42.77},
  {region:"South East",year:2022,admissions:105738,pop:9200000,rate:1149.33,pm25:8.93,no2:20.37,o3:48.97},
  {region:"South West",year:2022,admissions:63030,pop:5600000,rate:1125.55,pm25:7.46,no2:17.01,o3:51.7},
  {region:"North East and Yorkshire",year:2022,admissions:116138,pop:8100000,rate:1433.81,pm25:8.63,no2:23.23,o3:52.74},
  {region:"London",year:2023,admissions:111063,pop:9000000,rate:1234.04,pm25:10.38,no2:24.44,o3:41.77},
  {region:"North West",year:2023,admissions:101655,pop:7300000,rate:1392.54,pm25:8.16,no2:20.25,o3:48.78},
  {region:"Midlands",year:2023,admissions:144348,pop:10800000,rate:1336.56,pm25:9.21,no2:24.68,o3:46.22},
  {region:"East of England",year:2023,admissions:73952,pop:6200000,rate:1192.78,pm25:8.71,no2:21.24,o3:55.1},
  {region:"South East",year:2023,admissions:98995,pop:9200000,rate:1076.04,pm25:8.71,no2:20.07,o3:43.72},
  {region:"South West",year:2023,admissions:58616,pop:5600000,rate:1046.72,pm25:6.96,no2:16.96,o3:51.7},
  {region:"North East and Yorkshire",year:2023,admissions:106003,pop:8100000,rate:1308.68,pm25:8.47,no2:21.03,o3:44.76}
];

const REGIONS = [...new Set(DATA.map(d => d.region))];
const YEARS = [...new Set(DATA.map(d => d.year))].sort();
const COLORS = ['#3b82f6','#f59e0b','#10b981','#8b5cf6','#ef4444','#06b6d4','#ec4899'];
const LAYOUT_BASE = {
    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(26,34,54,0.6)',
    font: { family: 'Inter, sans-serif', color: '#94a3b8', size: 13 },
    margin: { t: 40, r: 30, b: 50, l: 60 },
    xaxis: { gridcolor: 'rgba(148,163,184,0.08)', zerolinecolor: 'rgba(148,163,184,0.15)' },
    yaxis: { gridcolor: 'rgba(148,163,184,0.08)', zerolinecolor: 'rgba(148,163,184,0.15)' },
    legend: { font: { size: 11 } },
};
const CFG = { responsive: true, displayModeBar: true, displaylogo: false,
    modeBarButtonsToRemove: ['lasso2d','select2d','autoScale2d'] };

// ── 1. TIME SERIES ──
function renderTimeSeries() {
    const traces = REGIONS.map((r, i) => {
        const rd = DATA.filter(d => d.region === r);
        return { x: rd.map(d => d.year), y: rd.map(d => d.pm25), name: r, type: 'scatter',
            mode: 'lines+markers', line: { width: 3, color: COLORS[i] },
            marker: { size: 8 }, hovertemplate: `<b>${r}</b><br>%{x}: %{y:.2f} μg/m³<extra></extra>` };
    });
    Plotly.newPlot('chart-timeseries', traces, {
        ...LAYOUT_BASE, xaxis: { ...LAYOUT_BASE.xaxis, title: 'Year', dtick: 1 },
        yaxis: { ...LAYOUT_BASE.yaxis, title: 'PM2.5 (μg/m³)' },
        legend: { ...LAYOUT_BASE.legend, orientation: 'h', y: -0.2 }
    }, CFG);
}

// ── 2. BAR CHART (avg admissions) ──
function renderBarAdmissions() {
    const avgRates = REGIONS.map(r => {
        const rd = DATA.filter(d => d.region === r);
        return { region: r, avg: rd.reduce((s, d) => s + d.rate, 0) / rd.length };
    }).sort((a, b) => b.avg - a.avg);
    Plotly.newPlot('chart-bar-admissions', [{
        x: avgRates.map(d => d.region), y: avgRates.map(d => d.avg), type: 'bar',
        marker: { color: avgRates.map((_, i) => COLORS[i]), cornerradius: 6 },
        hovertemplate: '<b>%{x}</b><br>%{y:.1f} per 100k<extra></extra>'
    }], {
        ...LAYOUT_BASE,
        xaxis: { ...LAYOUT_BASE.xaxis, tickangle: -25 },
        yaxis: { ...LAYOUT_BASE.yaxis, title: 'Avg Admission Rate (per 100k)' }
    }, CFG);
}

// ── 3. SCATTER PM2.5 vs ADMISSIONS ──
function renderScatter() {
    const traces = REGIONS.map((r, i) => {
        const rd = DATA.filter(d => d.region === r);
        return { x: rd.map(d => d.pm25), y: rd.map(d => d.rate), name: r, type: 'scatter',
            mode: 'markers', marker: { size: 12, color: COLORS[i], opacity: 0.85,
            line: { width: 1.5, color: '#fff' } },
            hovertemplate: `<b>${r}</b><br>PM2.5: %{x:.2f}<br>Rate: %{y:.1f}<extra></extra>` };
    });
    // trend line
    const xs = DATA.map(d => d.pm25), ys = DATA.map(d => d.rate);
    const n = xs.length, mx = xs.reduce((a,b)=>a+b)/n, my = ys.reduce((a,b)=>a+b)/n;
    const num = xs.reduce((s,x,i) => s + (x-mx)*(ys[i]-my), 0);
    const den = xs.reduce((s,x) => s + (x-mx)**2, 0);
    const slope = num/den, intercept = my - slope*mx;
    const xMin = Math.min(...xs), xMax = Math.max(...xs);
    traces.push({ x: [xMin, xMax], y: [slope*xMin+intercept, slope*xMax+intercept],
        mode: 'lines', line: { color: '#ef4444', width: 2.5, dash: 'dash' },
        name: 'Trend', showlegend: true });
    Plotly.newPlot('chart-scatter', traces, {
        ...LAYOUT_BASE,
        xaxis: { ...LAYOUT_BASE.xaxis, title: 'PM2.5 (μg/m³)' },
        yaxis: { ...LAYOUT_BASE.yaxis, title: 'Admission Rate (per 100k)' },
        legend: { ...LAYOUT_BASE.legend, orientation: 'h', y: -0.2 }
    }, CFG);
}

// ── 4. HEATMAP ──
function renderHeatmap() {
    const vars = ['pm25','no2','o3','rate'];
    const labels = ['PM2.5','NO2','O3','Admissions'];
    function corr(a, b) {
        const n=a.length, ma=a.reduce((s,v)=>s+v)/n, mb=b.reduce((s,v)=>s+v)/n;
        const num=a.reduce((s,v,i)=>s+(v-ma)*(b[i]-mb),0);
        const da=Math.sqrt(a.reduce((s,v)=>s+(v-ma)**2,0));
        const db=Math.sqrt(b.reduce((s,v)=>s+(v-mb)**2,0));
        return num/(da*db);
    }
    const z = vars.map(v1 => vars.map(v2 => +corr(DATA.map(d=>d[v1]), DATA.map(d=>d[v2])).toFixed(3)));
    Plotly.newPlot('chart-heatmap', [{
        z, x: labels, y: labels, type: 'heatmap', colorscale: [[0,'#1e3a5f'],[0.5,'#1a2236'],[1,'#f59e0b']],
        zmin: -1, zmax: 1, hovertemplate: '%{y} × %{x}: %{z:.3f}<extra></extra>',
        text: z.map(r => r.map(v => v.toFixed(2))), texttemplate: '%{text}', textfont: { color: '#f1f5f9', size: 14 }
    }], { ...LAYOUT_BASE, margin: { t: 20, r: 20, b: 60, l: 80 },
        xaxis: { ...LAYOUT_BASE.xaxis, side: 'bottom' },
        yaxis: { ...LAYOUT_BASE.yaxis, autorange: 'reversed' } }, CFG);
}

// ── 5. RADAR ──
function renderRadar() {
    const d2023 = DATA.filter(d => d.year === 2023);
    const traces = d2023.map((d, i) => ({
        type: 'scatterpolar', r: [d.pm25, d.no2, d.o3, d.pm25],
        theta: ['PM2.5','NO2','O3','PM2.5'], fill: 'toself',
        fillcolor: COLORS[i] + '22', line: { color: COLORS[i], width: 2 },
        name: d.region,
        hovertemplate: `<b>${d.region}</b><br>%{theta}: %{r:.2f}<extra></extra>`
    }));
    Plotly.newPlot('chart-radar', traces, {
        ...LAYOUT_BASE,
        polar: { bgcolor: 'rgba(26,34,54,0.6)',
            radialaxis: { gridcolor: 'rgba(148,163,184,0.15)', color: '#94a3b8' },
            angularaxis: { gridcolor: 'rgba(148,163,184,0.15)', color: '#f1f5f9' } },
        legend: { ...LAYOUT_BASE.legend, orientation: 'h', y: -0.15 }
    }, CFG);
}

// ── 6. COEFFICIENT PLOT ──
function renderCoefficients() {
    const names = ['PM2.5','NO2','O3'];
    const coefs = [39.99, -3.58, 2.02];
    const ciLow = [-0.36, -11.87, -2.14];
    const ciHigh = [80.35, 4.70, 6.18];
    const colors = coefs.map(c => c > 0 ? '#f59e0b' : '#3b82f6');
    Plotly.newPlot('chart-coefficients', [{
        x: coefs, y: names, type: 'bar', orientation: 'h',
        marker: { color: colors, cornerradius: 6 },
        error_x: { type: 'data', symmetric: false,
            array: coefs.map((c,i) => ciHigh[i]-c), arrayminus: coefs.map((c,i) => c-ciLow[i]),
            color: '#f1f5f9', thickness: 2, width: 8 },
        hovertemplate: '<b>%{y}</b><br>Coef: %{x:.2f}<extra></extra>'
    }], {
        ...LAYOUT_BASE,
        xaxis: { ...LAYOUT_BASE.xaxis, title: 'Coefficient (Impact on Admissions per 100k)', zeroline: true, zerolinewidth: 2, zerolinecolor: '#64748b' },
        yaxis: { ...LAYOUT_BASE.yaxis },
        shapes: [{ type: 'line', x0: 0, x1: 0, y0: -0.5, y1: 2.5, line: { color: '#64748b', width: 1.5, dash: 'dash' } }]
    }, CFG);
}

// ── 7. REGION FIXED EFFECTS ──
function renderRegionFE() {
    const regions = ['North West','North East and Yorkshire','Midlands','London','South East','South West'];
    const coefs = [244.72, 234.68, 114.88, 35.00, -72.47, -74.00];
    const colors = coefs.map(c => c > 0 ? '#ef4444' : '#10b981');
    Plotly.newPlot('chart-region-fe', [{
        x: regions, y: coefs, type: 'bar',
        marker: { color: colors, cornerradius: 6 },
        hovertemplate: '<b>%{x}</b><br>Baseline shift: %{y:+.1f} per 100k<extra></extra>'
    }], {
        ...LAYOUT_BASE,
        xaxis: { ...LAYOUT_BASE.xaxis, tickangle: -20 },
        yaxis: { ...LAYOUT_BASE.yaxis, title: 'Coefficient vs East of England (ref)', zeroline: true, zerolinewidth: 2, zerolinecolor: '#64748b' },
        shapes: [{ type: 'line', x0: -0.5, x1: 5.5, y0: 0, y1: 0, line: { color: '#64748b', width: 1.5, dash: 'dash' } }]
    }, CFG);
}

// ── 8. YEAR FIXED EFFECTS ──
function renderYearFE() {
    const years = [2016,2017,2018,2019,2020,2021,2022,2023];
    const coefs = [-35.10,-74.93,-77.20,-76.37,-309.97,-318.31,-130.60,-157.92];
    const colors = coefs.map(c => {
        if (c < -200) return '#ef4444';
        if (c < -100) return '#f59e0b';
        return '#3b82f6';
    });
    Plotly.newPlot('chart-year-fe', [{
        x: years, y: coefs, type: 'bar',
        marker: { color: colors, cornerradius: 6 },
        hovertemplate: 'Year %{x}<br>Shift: %{y:+.1f} per 100k<extra></extra>'
    }], {
        ...LAYOUT_BASE,
        xaxis: { ...LAYOUT_BASE.xaxis, title: 'Year', dtick: 1 },
        yaxis: { ...LAYOUT_BASE.yaxis, title: 'Coefficient vs 2015 (ref)' },
        shapes: [{ type: 'line', x0: 2015.5, x1: 2023.5, y0: 0, y1: 0, line: { color: '#64748b', width: 1.5, dash: 'dash' } }],
        annotations: [{ x: 2020, y: -309.97, text: 'COVID-19', showarrow: true, arrowhead: 2, arrowcolor: '#ef4444', font: { color: '#ef4444', size: 12 }, ay: -40 }]
    }, CFG);
}

// ── 9. RESIDUALS ──
function renderResiduals() {
    // Simple predicted = intercept + coefs * pollutants (from fixed effects)
    const intercept = 949.84;
    const regionCoefs = {"East of England":0,"London":35,"Midlands":114.88,"North East and Yorkshire":234.68,"North West":244.72,"South East":-72.47,"South West":-74};
    const yearCoefs = {2015:0,2016:-35.1,2017:-74.93,2018:-77.2,2019:-76.37,2020:-309.97,2021:-318.31,2022:-130.6,2023:-157.92};
    const predicted = DATA.map(d => intercept + 39.99*d.pm25 + (-3.58)*d.no2 + 2.02*d.o3 + (regionCoefs[d.region]||0) + (yearCoefs[d.year]||0));
    const residuals = DATA.map((d, i) => d.rate - predicted[i]);
    const traces = REGIONS.map((r, i) => {
        const rd = DATA.filter(d => d.region === r);
        const r_predicted = rd.map(d => intercept + 39.99*d.pm25 + (-3.58)*d.no2 + 2.02*d.o3 + (regionCoefs[d.region]||0) + (yearCoefs[d.year]||0));
        const r_residuals = rd.map((d, j) => d.rate - r_predicted[j]);
        return {
            x: r_predicted, y: r_residuals, name: r, mode: 'markers', type: 'scatter',
            marker: { size: 10, color: COLORS[i], opacity: 0.85, line: { width: 1.5, color: '#fff' } },
            text: rd.map(d => `${d.region} (${d.year})`),
            hovertemplate: '<b>%{text}</b><br>Predicted: %{x:.1f}<br>Residual: %{y:.1f}<extra></extra>'
        };
    });
    Plotly.newPlot('chart-residuals', traces, {
        ...LAYOUT_BASE,
        xaxis: { ...LAYOUT_BASE.xaxis, title: 'Predicted Admission Rate' },
        yaxis: { ...LAYOUT_BASE.yaxis, title: 'Residual' },
        shapes: [{ type: 'line', x0: Math.min(...predicted)-20, x1: Math.max(...predicted)+20, y0: 0, y1: 0, line: { color: '#64748b', width: 1.5, dash: 'dash' } }]
    }, CFG);
}

// ── INIT ──
document.addEventListener('DOMContentLoaded', () => {
    renderTimeSeries();
    renderBarAdmissions();
    renderScatter();
    renderHeatmap();
    renderRadar();
    renderCoefficients();
    renderRegionFE();
    renderYearFE();
    renderResiduals();
});
