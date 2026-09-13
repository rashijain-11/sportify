from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.contrib.auth.models import User
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds database with 40 realistic sports categories, products (INR pricing), and demo admin user'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Starting Sportify database expansion (INR pricing)..."))

        # 1. Create a demo superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@sportify.com', 'admin123')
            self.stdout.write(self.style.SUCCESS("Created demo admin user: username='admin', password='admin123'"))

        # 2. Categories Data (8 Sports Categories)
        categories_data = [
            {
                'name': 'Cricket',
                'description': 'Premium English & Kashmir willow bats, leather match balls, batting pads, gloves, and protective helmets.',
                'icon': 'bi-trophy',
                'image_url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Football',
                'description': 'Pro match footballs, goalkeeper gloves, shin guards, studs/boots, and training agility gear.',
                'icon': 'bi-dribbble',
                'image_url': 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Basketball',
                'description': 'Indoor & outdoor composite basketballs, rims, nets, court shoes, arm sleeves, and jerseys.',
                'icon': 'bi-circle',
                'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Badminton',
                'description': 'Ultra-light graphite rackets, goose feather shuttles, kit bags, non-marking shoes, and grips.',
                'icon': 'bi-bullseye',
                'image_url': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Tennis',
                'description': 'High-performance tour graphite rackets, pressurized match balls, tour bags, and overgrips.',
                'icon': 'bi-disc',
                'image_url': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Gym & Fitness',
                'description': 'Cast iron & rubber dumbbells, resistance loops, speed jump ropes, yoga mats, and strength training gear.',
                'icon': 'bi-heart-pulse',
                'image_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Running',
                'description': 'Carbon-plated cushioned running shoes, hydration vests, compression socks, and lightweight sports gear.',
                'icon': 'bi-lightning',
                'image_url': 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=800&auto=format&fit=crop&q=80'
            },
            {
                'name': 'Sports Accessories',
                'description': 'Insulated stainless steel bottles, gym duffels, wristbands, stopwatches, and joint support sleeves.',
                'icon': 'bi-backpack',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
        ]

        created_categories = {}
        for cat_data in categories_data:
            category, _ = Category.objects.update_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            created_categories[category.name] = category

        # 3. Expanded Products Data (40 Realistic Sports Products)
        products_data = [
            # ================= CRICKET (5 Items) =================
            {
                'category': created_categories['Cricket'],
                'name': 'Apex Pro English Willow Cricket Bat',
                'description': 'Handcrafted Grade 1 English willow cricket bat designed for explosive stroke play. Features an enlarged sweet spot, light pickup, and pre-knocked finish for immediate match readiness.',
                'price': Decimal('7999.00'),
                'discount_price': Decimal('5999.00'),
                'stock': 15,
                'rating': Decimal('4.9'),
                'review_count': 38,
                'is_featured': True,
                'sizes': 'Short Handle, Long Handle, Harrow',
                'image_url': 'https://images.unsplash.com/photo-1624526267942-ab0ff8a3e972?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Cricket'],
                'name': 'Match Grade Leather Cricket Ball (Box of 2)',
                'description': 'Four-piece alum-tanned premium leather ball with pronounced seam for maximum swing and bounce. Ideal for competitive club cricket and multi-day tournaments.',
                'price': Decimal('1499.00'),
                'discount_price': Decimal('1199.00'),
                'stock': 40,
                'rating': Decimal('4.7'),
                'review_count': 22,
                'is_featured': False,
                'sizes': 'Red (Day), White (D/N), Pink',
                'image_url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Cricket'],
                'name': 'Aero Armor Pro Batting Gloves',
                'description': 'Multi-split finger protection with high-density EVA foam and Pittards sheepskin leather palm for supreme grip and comfort against 90mph bowling.',
                'price': Decimal('1899.00'),
                'discount_price': Decimal('1499.00'),
                'stock': 25,
                'rating': Decimal('4.8'),
                'review_count': 19,
                'is_featured': False,
                'sizes': 'Youth, Men, Extra Large',
                'image_url': 'https://images.unsplash.com/photo-1624880357913-a8539238245b?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Cricket'],
                'name': 'ShieldTech Lightweight Batting Legguards',
                'description': 'Ultra-lightweight molded cane front with triple-layer knee bolster and air-cooled mesh lining. Provides top-tier protection without restricting running between wickets.',
                'price': Decimal('3299.00'),
                'discount_price': Decimal('2499.00'),
                'stock': 20,
                'rating': Decimal('4.8'),
                'review_count': 14,
                'is_featured': False,
                'sizes': 'Boys, Youth, Men',
                'image_url': 'https://images.unsplash.com/photo-1593341646782-e0b495cff86d?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Cricket'],
                'name': 'Titanium Pro Cricket Helmet with Steel Visor',
                'description': 'High-impact outer ABS shell with reinforced steel face grille and quick-dial adjustment system. Certified to official international cricket safety standards.',
                'price': Decimal('2899.00'),
                'discount_price': Decimal('2199.00'),
                'stock': 18,
                'rating': Decimal('4.9'),
                'review_count': 27,
                'is_featured': True,
                'sizes': 'Small (54-56cm), Medium (57-58cm), Large (59-62cm)',
                'image_url': 'https://images.unsplash.com/photo-1593341646782-e0b495cff86d?w=800&auto=format&fit=crop&q=80'
            },

            # ================= FOOTBALL (5 Items) =================
            {
                'category': created_categories['Football'],
                'name': 'Strikeforce FIFA Pro Match Football',
                'description': 'Thermally bonded seamless surface construction for more predictable trajectory, enhanced touch, and lower water uptake. Officially approved for tournament play.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1899.00'),
                'stock': 30,
                'rating': Decimal('4.9'),
                'review_count': 45,
                'is_featured': True,
                'sizes': 'Size 5 (Standard), Size 4 (Youth)',
                'image_url': 'https://images.unsplash.com/photo-1511886929837-354d827aae26?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Football'],
                'name': 'Vortex Grip Goalkeeper Match Gloves',
                'description': '4mm German contact latex foam offers dependable cushioning and unrivaled stickiness in both wet and dry conditions. Features negative cut finger spines.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('2399.00'),
                'stock': 20,
                'rating': Decimal('4.8'),
                'review_count': 29,
                'is_featured': False,
                'sizes': 'Size 8, Size 9, Size 10, Size 11',
                'image_url': 'https://images.unsplash.com/photo-1589487391730-58f20eb2c308?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Football'],
                'name': 'Predator Strike Firm Ground Football Boots',
                'description': 'High-tensile synthetic upper with embossed striking zones for spin control. Lightweight TPU outsole with conical studs offers razor-sharp traction on natural grass.',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3799.00'),
                'stock': 22,
                'rating': Decimal('4.9'),
                'review_count': 51,
                'is_featured': True,
                'sizes': 'UK 7, UK 8, UK 9, UK 10, UK 11',
                'image_url': 'https://images.unsplash.com/photo-1511886929837-354d827aae26?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Football'],
                'name': 'ImpactGuard Pro Ankle Shin Guards',
                'description': 'Anatomical low-profile polypropylene shell backed with thick EVA foam padding for robust shock dispersal. Includes breathable compression calf sleeve.',
                'price': Decimal('899.00'),
                'discount_price': Decimal('649.00'),
                'stock': 40,
                'rating': Decimal('4.6'),
                'review_count': 18,
                'is_featured': False,
                'sizes': 'Small, Medium, Large',
                'image_url': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Football'],
                'name': 'Speed & Agility Training Marker Cones (Set of 20)',
                'description': 'Flexible, shatterproof bright PE disc cones with steel carry handle. Essential for dribbling drills, shuttle sprints, and tactical boundary marking.',
                'price': Decimal('999.00'),
                'discount_price': Decimal('699.00'),
                'stock': 50,
                'rating': Decimal('4.7'),
                'review_count': 33,
                'is_featured': False,
                'sizes': 'Set of 20, Set of 50',
                'image_url': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop&q=80'
            },

            # ================= BASKETBALL (5 Items) =================
            {
                'category': created_categories['Basketball'],
                'name': 'PureBounce All-Court Composite Basketball',
                'description': 'Deep channel grooves and moisture-absorbing micro-fiber composite cover provide superior feel and precision control on indoor hardwood and outdoor concrete courts.',
                'price': Decimal('1999.00'),
                'discount_price': Decimal('1499.00'),
                'stock': 35,
                'rating': Decimal('4.8'),
                'review_count': 34,
                'is_featured': True,
                'sizes': 'Size 7 (Official), Size 6 (Women/Youth)',
                'image_url': 'https://images.unsplash.com/photo-1519861531473-9200262188bf?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Basketball'],
                'name': 'Velocity Slam Breathable Mesh Jersey',
                'description': 'Lightweight moisture-wicking Dri-Tech fabric keeps you cool and dry through fast breaks and overtime. Athletic cut allows unrestricted jumping and shooting motion.',
                'price': Decimal('1299.00'),
                'discount_price': None,
                'stock': 25,
                'rating': Decimal('4.6'),
                'review_count': 16,
                'is_featured': False,
                'sizes': 'S, M, L, XL, XXL',
                'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Basketball'],
                'name': 'DunkMaster High-Top Basketball Shoes',
                'description': 'Engineered with responsive Zoom air cushioning and padded collar for superior ankle lockdown during sharp crossovers and hard rebound landings.',
                'price': Decimal('5499.00'),
                'discount_price': Decimal('4299.00'),
                'stock': 20,
                'rating': Decimal('4.9'),
                'review_count': 42,
                'is_featured': True,
                'sizes': 'UK 7, UK 8, UK 9, UK 10, UK 11, UK 12',
                'image_url': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Basketball'],
                'name': 'Heavy-Duty Breakaway Basketball Rim & Net',
                'description': 'Solid steel 18-inch regulation rim with dual spring-loaded flex mechanism to absorb dunk forces. Includes all-weather braided nylon net.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('2299.00'),
                'stock': 15,
                'rating': Decimal('4.7'),
                'review_count': 19,
                'is_featured': False,
                'sizes': 'Standard Regulation 18"',
                'image_url': 'https://images.unsplash.com/photo-1574623452334-1e0ac2b3ccb4?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Basketball'],
                'name': 'Shooter Compression Arm Sleeves (Pair)',
                'description': 'Graduated compression improves blood circulation in the shooting arm and accelerates recovery. Non-slip silicone bands ensure a secure fit throughout games.',
                'price': Decimal('799.00'),
                'discount_price': Decimal('499.00'),
                'stock': 45,
                'rating': Decimal('4.8'),
                'review_count': 28,
                'is_featured': False,
                'sizes': 'M, L, XL',
                'image_url': 'https://images.unsplash.com/photo-1518063319789-7217e6706b04?w=800&auto=format&fit=crop&q=80'
            },

            # ================= BADMINTON (5 Items) =================
            {
                'category': created_categories['Badminton'],
                'name': 'AeroSpeed Ultra-Light Carbon Racket 4U',
                'description': 'High-modulus Japanese graphite frame with isometric head geometry expands sweet spot by 32%. Engineered for lightning-fast defensive returns and thunderous smashes.',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3699.00'),
                'stock': 18,
                'rating': Decimal('4.9'),
                'review_count': 41,
                'is_featured': True,
                'sizes': 'G4 (Medium), G5 (Thin)',
                'image_url': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Badminton'],
                'name': 'GrandPrix Goose Feather Shuttlecocks (Tube of 12)',
                'description': 'Selected Grade-A goose feathers mounted on solid natural Portuguese cork base for pinpoint flight stability and true trajectory in competitive matches.',
                'price': Decimal('1499.00'),
                'discount_price': Decimal('1199.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 53,
                'is_featured': False,
                'sizes': 'Speed 77 (Standard), Speed 78 (Fast)',
                'image_url': 'https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Badminton'],
                'name': 'ProCourt Non-Marking Indoor Badminton Shoes',
                'description': 'Gum rubber sole engineered with hexagonal grip pattern for instantaneous lateral agility. Features anti-torsion TPU midfoot shank and shock-dampening heel insert.',
                'price': Decimal('3999.00'),
                'discount_price': Decimal('2999.00'),
                'stock': 25,
                'rating': Decimal('4.8'),
                'review_count': 37,
                'is_featured': True,
                'sizes': 'UK 6, UK 7, UK 8, UK 9, UK 10, UK 11',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Badminton'],
                'name': 'Thermal Guard 6-Racket Tournament Kit Bag',
                'description': 'Dual main compartments with thermal foil insulation to protect string tension from ambient temperature shifts. Features ventilated shoe tunnel and backpack straps.',
                'price': Decimal('2699.00'),
                'discount_price': Decimal('1999.00'),
                'stock': 20,
                'rating': Decimal('4.7'),
                'review_count': 21,
                'is_featured': False,
                'sizes': '6-Racket Capacity',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Badminton'],
                'name': 'Tacky Overgrip Tape Pack of 5',
                'description': 'Super-absorbent polyurethane overgrip with micro-perforations to wick palm perspiration during high-intensity rallies.',
                'price': Decimal('699.00'),
                'discount_price': Decimal('449.00'),
                'stock': 60,
                'rating': Decimal('4.9'),
                'review_count': 64,
                'is_featured': False,
                'sizes': 'Assorted Colors, All Black, All White',
                'image_url': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&auto=format&fit=crop&q=80'
            },

            # ================= TENNIS (5 Items) =================
            {
                'category': created_categories['Tennis'],
                'name': 'TourSpin Master Graphite Tennis Racket',
                'description': 'Engineered with aerodynamic beam design and 100 sq inch head size for extreme top-spin and laser-accurate baseline control. Pre-strung with premium synthetic gut.',
                'price': Decimal('8999.00'),
                'discount_price': Decimal('6999.00'),
                'stock': 12,
                'rating': Decimal('4.9'),
                'review_count': 27,
                'is_featured': True,
                'sizes': 'Grip 2 (4 1/4"), Grip 3 (4 3/8")',
                'image_url': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Tennis'],
                'name': 'Open Championship Tennis Balls (Can of 4)',
                'description': 'Pressurized tournament balls with heavy-duty woven felt cover designed to resist fluffing and maintain consistent bounce on all court surfaces.',
                'price': Decimal('699.00'),
                'discount_price': Decimal('549.00'),
                'stock': 60,
                'rating': Decimal('4.7'),
                'review_count': 36,
                'is_featured': False,
                'sizes': 'Single Can (4 Balls), 3-Pack Bundle',
                'image_url': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Tennis'],
                'name': 'CourtElite Tennis Backpack with Racket Holder',
                'description': 'Dedicated zippered racket pocket holds up to 2 rackets with handle covers. Spacious main compartment with organizer sleeves and separate dirty gear bag.',
                'price': Decimal('3299.00'),
                'discount_price': Decimal('2499.00'),
                'stock': 18,
                'rating': Decimal('4.8'),
                'review_count': 23,
                'is_featured': False,
                'sizes': 'Standard (32L)',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Tennis'],
                'name': 'Silicone Tennis Racket Vibration Dampeners (Pack of 3)',
                'description': 'Grooved silicone rubber dampeners reduce string vibration and harsh feedback, protecting your elbow from repetitive strain injury.',
                'price': Decimal('599.00'),
                'discount_price': Decimal('399.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 41,
                'is_featured': False,
                'sizes': 'Pack of 3',
                'image_url': 'https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Tennis'],
                'name': 'Grand Slam Performance Tennis Polo',
                'description': 'Tailored athletic polo shirt with raglan sleeves and UV 50+ sun protection. Quick-drying lightweight weave keeps body temperature regulated under blazing sun.',
                'price': Decimal('1699.00'),
                'discount_price': Decimal('1299.00'),
                'stock': 30,
                'rating': Decimal('4.7'),
                'review_count': 19,
                'is_featured': False,
                'sizes': 'S, M, L, XL, XXL',
                'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&auto=format&fit=crop&q=80'
            },

            # ================= GYM & FITNESS (5 Items) =================
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'HexGrip Rubber Encased Dumbbell Set',
                'description': 'Cast iron core with non-toxic odorless virgin rubber coating to protect floors and reduce noise. Anti-roll hexagonal shape with knurled ergonomic chrome handle.',
                'price': Decimal('3999.00'),
                'discount_price': Decimal('2999.00'),
                'stock': 22,
                'rating': Decimal('4.9'),
                'review_count': 64,
                'is_featured': True,
                'sizes': '5kg Pair, 10kg Pair, 15kg Pair',
                'image_url': 'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'ProFlex Resistance Loop Bands (Set of 5)',
                'description': '100% natural Malaysian latex bands offering 5 progressive resistance levels from X-Light (5 lbs) to X-Heavy (40 lbs). Includes mesh travel pouch and workout guide.',
                'price': Decimal('1299.00'),
                'discount_price': Decimal('899.00'),
                'stock': 45,
                'rating': Decimal('4.7'),
                'review_count': 49,
                'is_featured': False,
                'sizes': '5-Band Full Set',
                'image_url': 'https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'Speed Master Ball-Bearing Steel Jump Rope',
                'description': 'High-velocity 360-degree dual ball bearing mechanism prevents tangling and allows smooth double-unders. Includes adjustable 3-meter vinyl-coated steel cable.',
                'price': Decimal('999.00'),
                'discount_price': Decimal('699.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 38,
                'is_featured': False,
                'sizes': 'Adjustable 3M Cable',
                'image_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'EcoGrip 8mm Dual-Texture Exercise & Yoga Mat',
                'description': 'Extra-thick 8mm high-density TPE cushioning protects joints and spine during floor workouts, calisthenics, and yoga. Non-slip ripple grip surface.',
                'price': Decimal('1999.00'),
                'discount_price': Decimal('1499.00'),
                'stock': 30,
                'rating': Decimal('4.8'),
                'review_count': 52,
                'is_featured': True,
                'sizes': '183cm x 61cm x 8mm',
                'image_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Gym & Fitness'],
                'name': 'Adjustable Heavy Hand Grip Strengthener (10-60kg)',
                'description': 'Rotary dial allows tension adjustment between 10kg and 60kg. Built with heavy-duty alloy steel springs and rubberized ergonomic non-slip handle.',
                'price': Decimal('699.00'),
                'discount_price': Decimal('449.00'),
                'stock': 40,
                'rating': Decimal('4.7'),
                'review_count': 29,
                'is_featured': False,
                'sizes': 'Standard (10-60kg Tension)',
                'image_url': 'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=800&auto=format&fit=crop&q=80'
            },

            # ================= RUNNING (5 Items) =================
            {
                'category': created_categories['Running'],
                'name': 'CloudStride Carbon Running Shoes',
                'description': 'Full-length carbon fiber propulsion plate sandwiched in dual-density supercritical foam for ultra-responsive energy return and reduced leg fatigue over marathon distances.',
                'price': Decimal('6999.00'),
                'discount_price': Decimal('4999.00'),
                'stock': 28,
                'rating': Decimal('4.9'),
                'review_count': 58,
                'is_featured': True,
                'sizes': 'UK 7, UK 8, UK 9, UK 10, UK 11',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Running'],
                'name': 'Marathon HydroVent Hydration Vest',
                'description': 'Featherweight 180g breathable mesh vest with dual 500ml front soft flask pockets, rear bladder sleeve, and bounce-free zippered smartphone harness.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1899.00'),
                'stock': 20,
                'rating': Decimal('4.8'),
                'review_count': 23,
                'is_featured': False,
                'sizes': 'Small/Medium, Large/X-Large',
                'image_url': 'https://images.unsplash.com/photo-1530549387789-4c1017266635?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Running'],
                'name': 'Anti-Blister Running Compression Socks (Pack of 3)',
                'description': 'Seamless toe design with targeted plantar arch band and moisture-wicking CoolMax yarn to prevent blisters and reduce calf fatigue.',
                'price': Decimal('1199.00'),
                'discount_price': Decimal('849.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 44,
                'is_featured': False,
                'sizes': 'M (UK 6-8), L (UK 9-11)',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Running'],
                'name': 'Bounce-Free Slim Running Waist Belt Pouch',
                'description': 'Expandable waterproof Lycra belt fits large smartphones, energy gels, and keys. Features reflective safety piping and earphone cord pass-through.',
                'price': Decimal('799.00'),
                'discount_price': Decimal('549.00'),
                'stock': 40,
                'rating': Decimal('4.7'),
                'review_count': 31,
                'is_featured': False,
                'sizes': 'Adjustable Waist (26"-42")',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Running'],
                'name': 'PaceMaster GPS Sports Smartwatch & Heart Rate Tracker',
                'description': 'Built-in GPS tracks real-time running pace, distance, elevation, and VO2 max. 14-day battery life, 50m water resistance, and syncs with Strava and Apple Health.',
                'price': Decimal('8999.00'),
                'discount_price': Decimal('6499.00'),
                'stock': 15,
                'rating': Decimal('4.9'),
                'review_count': 62,
                'is_featured': True,
                'sizes': 'Obsidian Black, Cobalt Blue',
                'image_url': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80'
            },

            # ================= SPORTS ACCESSORIES (5 Items) =================
            {
                'category': created_categories['Sports Accessories'],
                'name': 'HydroArmor Vacuum Insulated Sports Bottle 32oz',
                'description': 'Double-wall 18/8 kitchen-grade stainless steel keeps beverages ice cold for 24 hours or piping hot for 12 hours. Features wide-mouth spout and silicone chug cap.',
                'price': Decimal('1299.00'),
                'discount_price': Decimal('899.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 72,
                'is_featured': True,
                'sizes': '750ml, 1000ml',
                'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Sports Accessories'],
                'name': 'Sportify Waterproof Multi-Pocket Gym Duffel',
                'description': 'Heavy-duty 900D ripstop fabric with dedicated ventilated shoe compartment, wet towel pocket, padded shoulder strap, and key fob clip. 45L capacity.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1799.00'),
                'stock': 35,
                'rating': Decimal('4.9'),
                'review_count': 61,
                'is_featured': False,
                'sizes': 'Medium (35L), Large (45L)',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Sports Accessories'],
                'name': 'Pro Referee & Coach Digital Stopwatch & Whistle Set',
                'description': 'Precision 1/100th second chronograph stopwatch with lap/split time memory and date/alarm display. Paired with a pealess stainless steel whistle.',
                'price': Decimal('899.00'),
                'discount_price': Decimal('599.00'),
                'stock': 40,
                'rating': Decimal('4.7'),
                'review_count': 26,
                'is_featured': False,
                'sizes': 'Standard Stopwatch + Whistle Kit',
                'image_url': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Sports Accessories'],
                'name': 'Fast-Dry Microfiber Sports Towel with Zip Pocket',
                'description': 'Absorbs 4x its weight in moisture and dries 3x faster than cotton. Corner zipper pocket securely holds locker keys, gym card, and phone.',
                'price': Decimal('699.00'),
                'discount_price': Decimal('449.00'),
                'stock': 50,
                'rating': Decimal('4.8'),
                'review_count': 39,
                'is_featured': False,
                'sizes': 'Compact (40x80cm), Full (60x120cm)',
                'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&auto=format&fit=crop&q=80'
            },
            {
                'category': created_categories['Sports Accessories'],
                'name': 'ProActive Knee & Patella Compression Support Sleeve',
                'description': 'Anatomical 3D circular knit with lateral spring stabilizers and silicone patella gel pad. Delivers targeted compression for running, basketball, and squats.',
                'price': Decimal('999.00'),
                'discount_price': Decimal('699.00'),
                'stock': 45,
                'rating': Decimal('4.9'),
                'review_count': 57,
                'is_featured': True,
                'sizes': 'M (35-41cm), L (42-47cm), XL (48-55cm)',
                'image_url': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&auto=format&fit=crop&q=80'
            }
        ]

        created_count = 0
        updated_count = 0

        for p_data in products_data:
            product, created = Product.objects.update_or_create(
                name=p_data['name'],
                defaults=p_data
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(products_data)} products ({created_count} created, {updated_count} updated)!"))
