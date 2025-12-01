# OFAC SDN List

Cryptocurrency addresses that appear in [OFAC's SDN list](https://sanctionslist.ofac.treas.gov/Home/SdnList).

Exports are available in JSON, TOML, CSV, and TXT under the [Releases](https://github.com/vile/ofac-sdn-list/releases/) tab ([latest release](https://github.com/vile/ofac-sdn-list/releases/latest)).

This repo's [workflow](https://github.com/vile/ofac-sdn-list/actions/workflows/convert.yml) checks for new addresses every day at 6AM UTC.
If new addresses are found, a new release is created.

## New Address Notifications

You can receive notifications by using Github's native Watch feature or by using a thirdparty service such as [NewReleases](https://newreleases.io/).

## FAQ

### What is the OFAC SDN?

> [A] list of individuals and companies owned or controlled by, or acting for or on behalf of, targeted countries. It also lists individuals, groups, and entities, such as terrorists and narcotics traffickers designated under programs that are not country-specific. Collectively, such individuals and companies are called "Specially Designated Nationals" or "SDNs." Their assets are blocked and U.S. persons are generally prohibited from dealing with them ([source](https://ofac.treasury.gov/faqs/topic/1631)).
