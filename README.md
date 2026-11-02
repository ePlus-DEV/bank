# BankHub

Personal payment profile, built for GitHub Pages and designed to grow into a multi-user SaaS.

## Live deployment

Publish the repository root using **Settings → Pages → Deploy from a branch → main / root**.

Default URL: https://eplus-dev.github.io/bank/

## Current MVP

- Responsive dark/light payment profile
- Account search and category filters
- Copy account number, account holder and full details
- VietQR image support
- Public static hosting without authentication

## Add a receiving account

Edit the `accounts` array in `index.html`. Replace the disabled example with verified public receiving details:

```js
{
  id: "primary",
  category: "bank",
  bank: "Your bank",
  bankId: "VIETQR_BANK_BIN",
  name: "ACCOUNT HOLDER",
  number: "ACCOUNT_NUMBER",
  note: "Optional transfer note",
  featured: true,
  enabled: true
}
```

Never commit credentials, OTPs, private identity documents, or private banking data. QR codes are generated through the third-party VietQR image endpoint; account information included in the URL is sent to that provider.

## Architecture roadmap

See [ROADMAP.md](docs/ROADMAP.md).

## License

Copyright © ePlus.DEV. All rights reserved unless a license is added.
