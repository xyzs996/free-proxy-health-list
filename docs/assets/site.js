document.querySelectorAll('[data-copy]').forEach(function(btn){
  btn.addEventListener('click', function(){
    var text = btn.getAttribute('data-copy');
    navigator.clipboard.writeText(text).then(function(){
      var original = btn.textContent;
      btn.textContent = 'Copied';
      btn.setAttribute('data-copied','');
      setTimeout(function(){ btn.textContent = original; btn.removeAttribute('data-copied'); }, 1600);
    });
  });
});
document.querySelectorAll('svg.trend').forEach(function(svg){
  var raw = svg.getAttribute('data-points');
  if(!raw) return;
  var points = raw.split(';').map(function(p){ var s = p.split('|'); return {x:s[0], y:s[1]}; });
  var geom = (svg.getAttribute('data-pad')||'0,0').split(',').map(Number);
  var padL = geom[0], plotW = geom[1];
  var cross = svg.querySelector('.crosshair'), cursor = svg.querySelector('.cursor');
  var line = svg.querySelector('polyline');
  var tip = document.createElement('div');
  tip.className = 'tooltip';
  tip.hidden = true;
  svg.parentNode.appendChild(tip);
  function locate(event){
    var box = svg.getBoundingClientRect();
    var ratio = (event.clientX - box.left) / box.width;
    var vb = svg.viewBox.baseVal.width;
    var vx = ratio * vb;
    var index = Math.round((vx - padL) / (plotW / (points.length - 1)));
    index = Math.max(0, Math.min(points.length - 1, index));
    var px = padL + index * (plotW / (points.length - 1));
    var coords = line.getAttribute('points').split(' ')[index];
    if(!coords) return;
    var py = Number(coords.split(',')[1]);
    cross.setAttribute('x1', px); cross.setAttribute('x2', px); cross.setAttribute('opacity','1');
    cursor.setAttribute('cx', px); cursor.setAttribute('cy', py); cursor.setAttribute('opacity','1');
    tip.hidden = false;
    tip.innerHTML = '<b>' + points[index].y + '</b><span>' + points[index].x + '</span>';
    tip.style.left = (px / vb * box.width) + 'px';
  }
  svg.addEventListener('pointermove', locate);
  svg.addEventListener('pointerleave', function(){
    cross.setAttribute('opacity','0'); cursor.setAttribute('opacity','0'); tip.hidden = true;
  });
});
