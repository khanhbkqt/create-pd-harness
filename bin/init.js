#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];

if (!projectName) {
  console.error('Error: Vui lòng cung cấp tên thư mục dự án.');
  console.error('Ví dụ: npx create-product-design-harness my-project');
  process.exit(1);
}

const targetPath = path.join(process.cwd(), projectName);

if (fs.existsSync(targetPath)) {
  console.error(`Error: Thư mục "${projectName}" đã tồn tại. Vui lòng chọn tên khác hoặc xóa thư mục cũ.`);
  process.exit(1);
}

console.log(`Đang khởi tạo Product Design Harness tại ${targetPath}...`);

// Thư mục gốc chứa template (repo này)
const sourcePath = path.join(__dirname, '..');

// Các file/folder không muốn copy sang project mới
const excludeList = ['node_modules', '.git', 'bin', 'package.json', 'package-lock.json'];

function copyRecursiveSync(src, dest) {
  const exists = fs.existsSync(src);
  const stats = exists && fs.statSync(src);
  const isDirectory = exists && stats.isDirectory();
  
  const basename = path.basename(src);
  if (excludeList.includes(basename)) {
    return;
  }

  // Prevent infinite loop if target is inside source
  if (src === targetPath) {
    return;
  }

  if (isDirectory) {
    fs.mkdirSync(dest);
    fs.readdirSync(src).forEach(function(childItemName) {
      copyRecursiveSync(path.join(src, childItemName), path.join(dest, childItemName));
    });
  } else {
    fs.copyFileSync(src, dest);
  }
}

try {
  copyRecursiveSync(sourcePath, targetPath);
  
  console.log(`\n✅ Khởi tạo thành công "${projectName}"!`);
  console.log('\n🚀 BƯỚC TIẾP THEO:');
  console.log('1. Di chuyển vào thư mục dự án:');
  console.log(`   cd ${projectName}`);
  console.log('\n2. Khởi động AI Agent:');
  console.log('   Mở thư mục này bằng Antigravity IDE (hoặc CLI).');
  console.log('   Sau đó gõ lệnh sau để bắt đầu định hình dự án:');
  console.log('   /project-bootstrapping');
  console.log('\n(Tùy chọn) Để chạy mockup UI cục bộ:');
  console.log('   cd mockups && npm install && npm run dev');
  console.log('\nHãy đọc file AGENTS.md để hiểu nguyên tắc và các workflows có sẵn.');
} catch (err) {
  console.error('Đã xảy ra lỗi trong quá trình khởi tạo:', err);
  process.exit(1);
}
